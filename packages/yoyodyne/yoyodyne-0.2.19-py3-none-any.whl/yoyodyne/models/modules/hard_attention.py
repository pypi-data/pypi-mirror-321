"""Hard attention module classes."""

from typing import Tuple, Union

import torch
from torch import nn

from ... import defaults
from . import base, rnn


class HardAttentionRNNDecoder(rnn.RNNDecoder):
    """Abstract base class for zeroth-order HMM hard attention RNN decoders."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Activates emission probs.
        self.output_proj = nn.Sequential(
            nn.Linear(self.output_size, self.output_size), nn.Tanh()
        )
        # Projects transition probabilities to depth of module.
        self.scale_encoded = nn.Linear(
            self.decoder_input_size, self.hidden_size
        )

    def forward(
        self,
        symbol: torch.Tensor,
        last_hiddens: Union[torch.Tensor, Tuple[torch.Tensor, torch.Tensor]],
        encoder_out: torch.Tensor,
        encoder_mask: torch.Tensor,
    ) -> base.ModuleOutput:
        """Single decode pass.

        Args:
            symbol (torch.Tensor): previously decoded symbol of shape (B x 1).
            last_hiddens (Tuple[torch.Tensor, torch.Tensor]): last hidden
                states from the decoder of shape
                (1 x B x decoder_dim, 1 x B x decoder_dim).
            encoder_out (torch.Tensor): encoded input sequence of shape
                (B x seq_len x encoder_dim).
            encoder_mask (torch.Tensor): mask for the encoded input batch of
                shape (B x seq_len).

        Returns:
            base.ModuleOutput: step-wise emission probabilities, alignment
                matrix, and hidden states of decoder.
        """
        embedded = self.embed(symbol)
        decoded, hiddens = self.module(embedded, last_hiddens)
        emissions = self._get_emissions(decoded, encoder_out)
        transitions = self._get_transitions(decoded, encoder_out, encoder_mask)
        return base.ModuleOutput(emissions, hiddens, embeddings=transitions)

    def _get_emissions(
        self, decoded: torch.Tensor, encoder_out: torch.Tensor
    ) -> torch.Tensor:
        """Gets emission probabilities for current timestep.

        Args:
            decoded (torch.Tensor): output from decoder for current timesstep
                of shape B x 1 x decoder_dim.
            encoder_out (torch.Tensor): encoded input sequence of shape
                B x seq_len x encoder_dim.

        Returns:
            torch.Tensor.
        """
        output = decoded.expand(-1, encoder_out.size(1), -1)
        output = torch.cat((output, encoder_out), dim=2)
        output = self.output_proj(output)
        return output

    def _get_transitions(
        self,
        decoded: torch.Tensor,
        encoder_out: torch.Tensor,
        encoder_mask: torch.Tensor,
    ) -> torch.Tensor:
        """Gets transition probabilities for current timestep.

        Given the current encoder representation and the decoder
        representation at the current time step, this calculates the alignment
        scores between all potential source sequence pairings. These
        alignments are used to predict the likelihood of state transitions
        for the output.

        After:
            Wu, S. and Cotterell, R. 2019. Exact hard monotonic attention for
            character-level transduction. In _Proceedings of the 57th Annual
            Meeting of the Association for Computational Linguistics_, pages
            1530-1537.

        Args:
            decoded (torch.Tensor): output from decoder for current timesstep
                of shape B x 1 x decoder_dim.
            encoder_out (torch.Tensor): encoded input sequence of shape
                B x seq_len x encoder_dim.
            encoder_mask (torch.Tensor): mask for the encoded input batch of
                shape B x seq_len.

        Returns:
            torch.Tensor: alignment scores across the source sequence of shape
                B x seq_len.
        """
        alignment_scores = torch.bmm(
            self.scale_encoded(encoder_out), decoded.transpose(1, 2)
        ).squeeze(2)
        # Gets probability of alignments.
        alignment_probs = nn.functional.softmax(alignment_scores, dim=1)
        # Masks padding.
        alignment_probs = alignment_probs * (~encoder_mask) + defaults.EPSILON
        alignment_probs = alignment_probs / alignment_probs.sum(
            dim=1, keepdim=True
        )
        # Expands over all time steps; uses log probabilities for quicker
        # computations.
        return (
            alignment_probs.log()
            .unsqueeze(1)
            .expand(-1, encoder_out.size(1), -1)
        )

    @property
    def output_size(self) -> int:
        return self.decoder_input_size + self.hidden_size


class HardAttentionGRUDecoder(HardAttentionRNNDecoder):
    """Zeroth-order HMM hard attention GRU decoder."""

    def get_module(self) -> nn.GRU:
        return nn.GRU(
            self.embedding_size,
            self.hidden_size,
            batch_first=True,
            bidirectional=self.bidirectional,
            dropout=self.dropout,
            num_layers=self.layers,
        )

    @property
    def name(self) -> str:
        return "hard attention GRU"


class HardAttentionLSTMDecoder(HardAttentionRNNDecoder):
    """Zeroth-order HMM hard attention LSTM decoder."""

    def get_module(self) -> nn.LSTM:
        return nn.LSTM(
            self.embedding_size,
            self.hidden_size,
            batch_first=True,
            bidirectional=self.bidirectional,
            dropout=self.dropout,
            num_layers=self.layers,
        )

    @property
    def name(self) -> str:
        return "hard attention LSTM"


class ContextHardAttentionRNNDecoder(HardAttentionRNNDecoder):
    """Abstract base class for first-order HMM hard attention RNN decoder."""

    def __init__(self, attention_context, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.delta = attention_context
        # The window size must include center and both sides.
        self.alignment_proj = nn.Linear(
            self.hidden_size * 2, (attention_context * 2) + 1
        )

    def _get_transitions(
        self,
        decoded: torch.Tensor,
        encoder_out: torch.Tensor,
        encoder_mask: torch.Tensor,
    ) -> torch.Tensor:
        """Gets transition probabilities for current timestep.

        Args:
            decoded (torch.Tensor): output from decoder for current timesstep
                of shape B x 1 x decoder_dim.
            encoder_out (torch.Tensor): encoded input sequence of shape
                B x seq_len x encoder_dim.
            encoder_mask (torch.Tensor): mask for the encoded input batch of
                shape B x seq_len.

        Returns:
            torch.Tensor: alignment scores across the source sequence of shape
                B x seq_len.
        """
        # Matrix multiplies encoding and decoding for alignment
        # representations. See: https://aclanthology.org/P19-1148/.
        # Expands decoded so it can concatenate with alignments.
        decoded = decoded.expand(-1, encoder_out.size(1), -1)
        # -> B x seq_len.
        alignment_scores = torch.cat(
            (self.scale_encoded(encoder_out), decoded), dim=2
        )
        alignment_scores = self.alignment_proj(alignment_scores)
        alignment_probs = nn.functional.softmax(alignment_scores, dim=1)
        # Limits context to a window of the size delta (i.e., the context
        # length).
        alignment_probs = alignment_probs.split(1, dim=1)
        alignment_probs = torch.cat(
            [
                nn.functional.pad(
                    t,
                    (
                        -self.delta + i,
                        encoder_mask.size(1) - (self.delta + 1) - i,
                    ),
                )
                for i, t in enumerate(alignment_probs)
            ],
            dim=1,
        )
        # Gets probability of alignments, masking padding.
        alignment_probs = (
            alignment_probs * (~encoder_mask).unsqueeze(1) + defaults.EPSILON
        )
        alignment_probs = alignment_probs / alignment_probs.sum(
            dim=2, keepdim=True
        )
        # Uses log probabilities for quicker computations.
        return alignment_probs.log()


class ContextHardAttentionGRUDecoder(
    ContextHardAttentionRNNDecoder, HardAttentionGRUDecoder
):
    """First-order HMM hard attention GRU decoder."""

    @property
    def name(self) -> str:
        return "contextual hard attention GRU"


class ContextHardAttentionLSTMDecoder(
    ContextHardAttentionRNNDecoder, HardAttentionLSTMDecoder
):
    """First-order HMM hard attention LSTM decoder."""

    @property
    def name(self) -> str:
        return "contextual hard attention LSTM"
