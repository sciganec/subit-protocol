# SUBIT-Agent Protocol — encoder.py
# Minimal SUBIT-Lingua v3.0 encoder
# Encodes forms, transitions, and sequences into 6-bit aligned bitstrings.

from typing import List, Union


class SubitEncoder:
    """
    Encodes SUBIT forms, transitions, and sequences into canonical bitstrings.
    - Form: integer 0–63  → 6 bits
    - Transition: tuple(formA, formB) → 12 bits
    - Sequence: list of forms → n×6 bits
    """

    @staticmethod
    def encode_form(value: int) -> str:
        if not (0 <= value <= 63):
            raise ValueError(f"Invalid SUBIT form: {value}")
        return format(value, "06b")

    @staticmethod
    def encode_transition(a: int, b: int) -> str:
        return SubitEncoder.encode_form(a) + SubitEncoder.encode_form(b)

    @staticmethod
    def encode_sequence(forms: List[int]) -> str:
        if not forms:
            raise ValueError("Sequence cannot be empty.")
        return "".join(SubitEncoder.encode_form(f) for f in forms)

    @staticmethod
    def encode(payload: Union[int, tuple, list]) -> str:
        """
        Universal encoder:
        - int → form
        - (a, b) → transition
        - [a, b, c...] → sequence
        """
        if isinstance(payload, int):
            return SubitEncoder.encode_form(payload)

        if isinstance(payload, tuple) and len(payload) == 2:
            return SubitEncoder.encode_transition(payload[0], payload[1])

        if isinstance(payload, list):
            return SubitEncoder.encode_sequence(payload)

        raise TypeError("Payload must be int, tuple(formA, formB), or list of forms.")
