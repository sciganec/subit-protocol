# SUBIT-Agent Protocol — validator.py
# Minimal structural validator for SUBIT-Lingua v3.0 packets.

from typing import List, Dict
from decoder import SubitDecoder


VALID_TYPES = {"STATE", "INTENT", "ACTION", "PLAN", "TRACE", "ERROR"}


class SubitValidator:
    """
    Validates:
    - Packet structure
    - SUBIT bitstring structure
    - Message-type constraints
    """

    # -----------------------------
    # Basic SUBIT validation
    # -----------------------------
    @staticmethod
    def validate_bitstring(bits: str):
        if not bits:
            raise ValueError("Payload cannot be empty.")
        if any(c not in "01" for c in bits):
            raise ValueError("Payload contains invalid characters.")
        if len(bits) % 6 != 0:
            raise ValueError("Payload length must be divisible by 6.")

    @staticmethod
    def validate_form(bits: str):
        if len(bits) != 6:
            raise ValueError("STATE or ERROR(form) must be exactly 6 bits.")
        SubitDecoder.decode_form(bits)

    @staticmethod
    def validate_transition(bits: str):
        if len(bits) != 12:
            raise ValueError("INTENT/ACTION transition must be exactly 12 bits.")
        SubitDecoder.decode_transition(bits)

    @staticmethod
    def validate_sequence(bits: str, min_forms: int):
        if len(bits) < min_forms * 6:
            raise ValueError(f"Sequence must contain at least {min_forms} forms.")
        SubitDecoder.decode_sequence(bits)

    # -----------------------------
    # Message-type validation
    # -----------------------------
    @staticmethod
    def validate_message_type(msg_type: str):
        if msg_type not in VALID_TYPES:
            raise ValueError(f"Invalid message type: {msg_type}")

    @staticmethod
    def validate_payload_for_type(msg_type: str, bits: str):
        # STATE
        if msg_type == "STATE":
            SubitValidator.validate_form(bits)
            return

        # INTENT
        if msg_type == "INTENT":
            if len(bits) < 12:
                raise ValueError("INTENT requires at least 12 bits.")
            return

        # ACTION
        if msg_type == "ACTION":
            SubitValidator.validate_transition(bits)
            return

        # PLAN
        if msg_type == "PLAN":
            SubitValidator.validate_sequence(bits, min_forms=3)
            return

        # TRACE
        if msg_type == "TRACE":
            SubitValidator.validate_sequence(bits, min_forms=2)
            return

        # ERROR
        if msg_type == "ERROR":
            if len(bits) not in (6, 12):
                raise ValueError("ERROR payload must be 6 or 12 bits.")
            return

    # -----------------------------
    # Packet validation
    # -----------------------------
    @staticmethod
    def validate_packet(packet: Dict):
        if "type" not in packet:
            raise ValueError("Packet missing 'type'.")
        if "payload" not in packet:
            raise ValueError("Packet missing 'payload'.")

        msg_type = packet["type"]
        bits = packet["payload"]

        SubitValidator.validate_message_type(msg_type)
        SubitValidator.validate_bitstring(bits)
        SubitValidator.validate_payload_for_type(msg_type, bits)

        return True

    # -----------------------------
    # Dialogue validation (optional)
    # -----------------------------
    @staticmethod
    def validate_dialogue_sequence(types: List[str]):
        """
        Validates a sequence of message types according to protocol rules.
        """
        if not types:
            raise ValueError("Dialogue cannot be empty.")

        if types[0] != "STATE":
            raise ValueError("Dialogue must begin with STATE.")

        for i in range(len(types) - 1):
            a, b = types[i], types[i + 1]

            # ERROR resets dialogue
            if a == "ERROR" and b != "STATE":
                raise ValueError("After ERROR, next message must be STATE.")

            # Forbidden transitions
            if a == "ACTION" and b in {"STATE", "INTENT"}:
                raise ValueError("ACTION cannot be followed by STATE or INTENT.")

            if a == "INTENT" and b == "STATE":
                raise ValueError("INTENT cannot be followed by STATE.")

            if a == "TRACE" and b in {"INTENT", "ACTION"}:
                raise ValueError("TRACE cannot be followed by INTENT or ACTION.")

            if a == "PLAN" and b == "INTENT":
                raise ValueError("PLAN cannot be followed by INTENT.")

        return True
