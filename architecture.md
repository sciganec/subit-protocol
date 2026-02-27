# **architecture.md**  
### **SUBIT‑Agent Protocol v1.0 — Architecture**

The SUBIT‑Agent Protocol is a layered communication system built on SUBIT‑Lingua v3.0.  
Each layer has a single responsibility: encoding, structuring, validating, interpreting, or executing agent communication.

---

## **1. Layer Overview**

The protocol consists of four architectural layers:

1. **Language Layer (SUBIT‑Lingua)**  
   Provides the atomic structural units: forms, transitions, sequences.

2. **Packet Layer (SUBIT‑Packets)**  
   Wraps SUBIT sequences into typed communication packets.

3. **Dialogue Layer (Interaction Engine)**  
   Defines valid message flows and reasoning patterns.

4. **Agent Layer (Behavior Engine)**  
   Interprets packets, updates internal state, and performs actions.

These layers form a deterministic pipeline from raw bits to agent behavior.

---

## **2. Language Layer (SUBIT‑Lingua)**

The language layer defines the structural primitives:

- **Form** — 6 bits  
- **Transition** — 12 bits  
- **Sequence** — n×6 bits  

This layer ensures:

- fixed structure  
- unambiguous parsing  
- deterministic encoding  
- universal representation  

All higher layers depend on this foundation.

---

## **3. Packet Layer (SUBIT‑Packets)**

The packet layer wraps SUBIT sequences into a unified message format:

```
{
  "type": "<MESSAGE_TYPE>",
  "payload": "<SUBIT_SEQUENCE>",
  "meta": { ... }
}
```

Responsibilities:

- define message types  
- enforce packet structure  
- ensure SUBIT‑valid payloads  
- provide metadata for routing and tracing  

This layer is transport‑agnostic and can be used over any channel.

---

## **4. Dialogue Layer (Interaction Engine)**

The dialogue layer defines how packets combine into structured exchanges.

Core patterns:

- **State → Intent → Action**  
- **Request → Response**  
- **Reasoning Chains**  
- **Multi‑Agent Flows**  
- **Error Recovery**  

Responsibilities:

- validate message transitions  
- enforce dialogue rules  
- maintain session coherence  
- structure reasoning sequences  

This layer ensures predictable, interpretable communication.

---

## **5. Agent Layer (Behavior Engine)**

The agent layer interprets packets and performs actions.

Responsibilities:

- decode SUBIT sequences  
- update internal state  
- generate intents and actions  
- execute plans  
- produce traces  
- handle errors  

This layer is implementation‑specific but must follow the protocol rules.

---

## **6. Data Flow**

A complete communication cycle follows this pipeline:

```
SUBIT Form/Sequence
        ↓
Packet Encoding
        ↓
Dialogue Pattern
        ↓
Agent Interpretation
        ↓
Action / Response
        ↓
New SUBIT Sequence
```

Each step is deterministic and reversible.

---

## **7. Minimal Reference Implementation**

The `src/` directory provides:

- `encoder.py` — SUBIT encoding  
- `decoder.py` — SUBIT decoding  
- `validator.py` — packet validation  
- `agent.py` — minimal agent implementing the architecture  

These components demonstrate the full architecture in practice.

---

## **8. Summary**

The SUBIT‑Agent Protocol architecture defines:

- a structural language layer  
- a unified packet layer  
- deterministic dialogue patterns  
- a behavior engine for agents  

This layered design ensures clarity, modularity, and universal interoperability across agent systems.

---
