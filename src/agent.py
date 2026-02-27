# SUBIT-Agent Protocol — agent.py
# Minimal reference agent implementing the SUBIT-Agent Protocol v1.0.
# Uses encoder, decoder, and validator to process packets structurally.

from typing import Dict
from encoder import SubitEncoder
from decoder import SubitDecoder
from validator import SubitValidator


class SubitAgent:
    """
    Minimal structural agent:
    - Maintains internal SUBIT state (single form)
    - Interprets STATE, INTENT, ACTION, PLAN, TRACE, ERROR
    - Produces ACTION or TRACE responses
    - No semantics: purely structural transformations
    """

    def __init__(self):
        self.state = None          # current SUBIT form (int)
        self.last_intent = None    # last transition (tuple)
        self.last_plan = None      # last sequence (list[int])
        self.error_flag = False

    # ---------------------------------------------------------
    # Packet creation helper
    # ---------------------------------------------------------
    @staticmethod
    def make_packet(msg_type: str, payload_bits: str) -> Dict:
        return {
            "type": msg_type,
            "payload": payload_bits,
            "meta": {}
        }

    # ---------------------------------------------------------
    # Core agent logic
    # ---------------------------------------------------------
    def process(self, packet: Dict) -> Dict:
        """
        Process a single SUBIT packet and return the next packet.
        """

        # Validate packet structure
        SubitValidator.validate_packet(packet)

        msg_type = packet["type"]
        bits = packet["payload"]

        # -----------------------------------------------------
        # ERROR resets the agent
        # -----------------------------------------------------
        if msg_type == "ERROR":
            self.state = None
            self.last_intent = None
            self.last_plan = None
            self.error_flag = True
            return self.make_packet("STATE", SubitEncoder.encode(0))  # reset to form 0

        # -----------------------------------------------------
        # STATE
        # -----------------------------------------------------
        if msg_type == "STATE":
            self.state = SubitDecoder.decode_form(bits)
            self.error_flag = False
            return self.make_packet("INTENT", self._generate_intent())

        # -----------------------------------------------------
        # INTENT
        # -----------------------------------------------------
        if msg_type == "INTENT":
            decoded = SubitDecoder.decode(bits)
            if isinstance(decoded, tuple):
                self.last_intent = decoded
            else:
                seq = SubitDecoder.decode_sequence(bits)
                self.last_intent = (seq[0], seq[1])
            return self.make_packet("ACTION", self._generate_action())

        # -----------------------------------------------------
        # ACTION
        # -----------------------------------------------------
        if msg_type == "ACTION":
            # Update internal state to the second form of the transition
            a, b = SubitDecoder.decode_transition(bits)
            self.state = b
            return self.make_packet("TRACE", self._generate_trace())

        # -----------------------------------------------------
        # PLAN
        # -----------------------------------------------------
        if msg_type == "PLAN":
            seq = SubitDecoder.decode_sequence(bits)
            self.last_plan = seq
            # Execute final transition of the plan
            final_transition = (seq[-2], seq[-1])
            self.state = final_transition[1]
            return self.make_packet("TRACE", self._generate_trace_from_plan(seq))

        # -----------------------------------------------------
        # TRACE (terminal)
        # -----------------------------------------------------
        if msg_type == "TRACE":
            return self.make_packet("STATE", SubitEncoder.encode(self.state))

        # Should never reach here
        raise ValueError(f"Unhandled message type: {msg_type}")

    # ---------------------------------------------------------
    # Internal generation helpers
    # ---------------------------------------------------------
    def _generate_intent(self) -> str:
        """
        Generate a simple intent: (state → state+1 mod 64)
        Purely structural, no semantics.
        """
        if self.state is None:
            raise ValueError("Cannot generate INTENT without STATE.")
        a = self.state
        b = (self.state + 1) % 64
        return SubitEncoder.encode((a, b))

    def _generate_action(self) -> str:
        """
        ACTION mirrors the last INTENT transition.
        """
        if not self.last_intent:
            raise ValueError("Cannot generate ACTION without INTENT.")
        return SubitEncoder.encode(self.last_intent)

    def _generate_trace(self) -> str:
        """
        TRACE is a simple 2-form explanation: [old_state, new_state].
        """
        a, b = self.last_intent
        return SubitEncoder.encode([a, b])

    def _generate_trace_from_plan(self, seq):
        """
        TRACE for PLAN: return the last 3 forms of the plan.
        """
        if len(seq) >= 3:
            return SubitEncoder.encode(seq[-3:])
        return SubitEncoder.encode(seq)
