# **README.md**  
### **SUBIT‑Agent Protocol v1.0**

SUBIT‑Agent Protocol is a structural communication standard built on top of SUBIT‑Lingua v3.0. It defines how agents encode state, intent, actions, plans, and reasoning chains using a deterministic, bit‑exact language of forms, transitions, and sequences.

The protocol provides a minimal, universal interface for agent‑to‑agent and agent‑to‑system communication.

---

## **Overview**

SUBIT‑Agent Protocol uses SUBIT‑Lingua as its transport layer:

- **Form** — 6‑bit atomic unit  
- **Word (Transition)** — 12‑bit pair of forms  
- **Sequence** — n×6‑bit structural chain  

All messages in the protocol are encoded as SUBIT sequences, ensuring full determinism, compactness, and unambiguous parsing.

The protocol defines:

- message types  
- packet format  
- dialogue patterns  
- validation rules  
- interpretation rules  
- reference implementation  

---

## **Key Concepts**

### **Message Types**
The protocol defines six universal message types:

- **STATE** — current agent state  
- **INTENT** — desired transition or goal  
- **ACTION** — executable operation  
- **PLAN** — structured multi‑step reasoning  
- **TRACE** — reasoning log  
- **ERROR** — structural or semantic error  

Each message carries a SUBIT sequence as its payload.

---

### **Packet Structure**

All communication uses a unified packet format:

```
{
  "type": "<MESSAGE_TYPE>",
  "payload": "<SUBIT_SEQUENCE>",
  "meta": {
      "agent": "<id>",
      "timestamp": "<iso8601>",
      "session": "<id>"
  }
}
```

Payloads are always SUBIT‑encoded forms, transitions, or sequences.

---

## **Dialogue Patterns**

The protocol supports deterministic communication flows:

- **Request → Response**  
- **State → Intent → Action**  
- **Reasoning Chains**  
- **Multi‑Agent Exchanges**  
- **Error Recovery**  

These patterns define how agents coordinate, negotiate, and execute tasks.

---

## **Validation**

Validation ensures structural correctness:

- bitstream length must be divisible by 6  
- each 6‑bit segment must decode to a valid SUBIT form  
- INTENT, ACTION, PLAN require ≥12 bits  
- packet type must be valid  
- dialogue transitions must follow protocol rules  

---

## **Interpretation**

Agents interpret messages through SUBIT‑Lingua:

- STATE → internal configuration  
- INTENT → desired transition  
- ACTION → executable step  
- PLAN → multi‑step reasoning  
- TRACE → explanation  
- ERROR → structural failure  

Interpretation is deterministic and reversible.

---

## **Repository Structure**

```
subit-agent-protocol/
│
├── README.md
├── protocol-spec.md
├── architecture.md
│
├── messages.md
├── dialogues.md
├── validation.md
├── interpretation.md
│
├── examples.md
│
└── src/
    ├── encoder.py
    ├── decoder.py
    ├── validator.py
    └── agent.py
```

---

## **Reference Implementation**

The `src/` directory includes minimal tools:

- `encoder.py` — SUBIT encoding  
- `decoder.py` — SUBIT decoding  
- `validator.py` — packet validation  
- `agent.py` — minimal agent implementing the protocol  

These components provide a baseline for integrating the protocol into larger systems.

---

## **License**

MIT License.

---
