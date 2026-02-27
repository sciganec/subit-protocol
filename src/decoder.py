# SUBIT-Agent Protocol — decoder.py
# Minimal SUBIT-Lingua v3.0 decoder
# Decodes 6-bit aligned bitstrings into forms, transitions, and sequences.

from typing import List, Union


class SubitDecoder:
    """
    Decodes SUBIT bitstrings into:
    - Form: 6 bits  → int (0–63)
    - Transition: 12 bits → (formA, formB)
    - Sequence: n×6 bits → list[int]
    """

    @staticmethod
    def _validate_bitstring(bits: str):
        if not bits:
            raise ValueError("Bitstring cannot be empty.")
        if any(c not in "01" for c in bits):
            raise ValueError("Bitstring contains invalid characters.")
        if len(bits) % 6 != 0:
            raise ValueError("Bitstring length must be divisible by 6.")

    @staticmethod
    def decode_form(bits: str) -> int:
        SubitDecoder._validate_bitstring(bits)
        if len(bits) != 6:
            raise ValueError("Form must be exactly 6 bits.")
        return int(bits, 2)

    @staticmethod
    def decode_transition(bits: str) -> tuple:
        SubitDecoder._validate_bitstring(bits)
        if len(bits) != 12:
            raise ValueError("Transition must be exactly 12 bits.")
        return (int(bits[:6], 2), int(bits[6:], 2))

    @staticmethod
    def decode_sequence(bits: str) -> List[int]:
        SubitDecoder._validate_bitstring(bits)
        return [int(bits[i:i+6], 2) for i in range(0, len(bits), 6)]

    @staticmethod
    def decode(bits: str) -> Union[int, tuple, List[int]]:
        """
        Universal decoder:
        - 6 bits → form
        - 12 bits → transition
        - n×6 bits → sequence
        """
        SubitDecoder._validate_bitstring(bits)

        if len(bits) == 6:
            return SubitDecoder.decode_form(bits)

        if len(bits) == 12:
            return SubitDecoder.decode_transition(bits)

        return SubitDecoder.decode_sequence(bits)
