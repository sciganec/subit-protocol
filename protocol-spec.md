# **protocol-spec.md**  
### **SUBIT‑Agent Protocol v1.0 — Formal Specification**

SUBIT‑Agent Protocol defines a structural communication layer built on SUBIT‑Lingua v3.0.  
All messages are encoded as SUBIT forms, transitions, or sequences, ensuring deterministic parsing and universal interoperability between agents.

---

## **1. Foundations**

SUBIT‑Lingua provides the transport primitives:

- **Form** — 6‑bit atomic unit  
- **Transition (Word)** — 12‑bit pair of forms  
- **Sequence** — n×6‑bit chain  

The protocol uses these primitives to encode state, intent, actions, plans, and reasoning traces.

---

## **2. Packet Format**

All communication uses a unified packet structure:

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

- `type` — required, one of the defined message types  
- `payload` — required, SUBIT‑encoded form/transition/sequence  
- `meta` — optional metadata  

Payloads must be valid SUBIT sequences (bit length divisible by 6).

---

## **3. Message Types**

The protocol defines six structural message types:

- **STATE** — current agent configuration (single form)  
- **INTENT** — desired transition or goal (transition or short sequence)  
- **ACTION** — executable operation (transition)  
- **PLAN** — multi‑step reasoning chain (sequence)  
- **TRACE** — explanation or log of reasoning (sequence)  
- **ERROR** — structural or semantic failure (form or short sequence)  

Each type is defined by its structural role, not semantics.

---

## **4. Payload Structure**

Payloads are always SUBIT‑encoded:

### **STATE**
```
<FORM>
```

### **INTENT / ACTION**
```
<FORM – FORM>
```

### **PLAN / TRACE**
```
<FORM – FORM – FORM ...>
```

### **ERROR**
```
<FORM> | <FORM – FORM>
```

Examples:

```
STATE: 000110
INTENT: 000110110001
PLAN: 000110 110001 011011
```

---

## **5. Dialogue Patterns**

The protocol defines deterministic communication flows.

### **5.1 State → Intent → Action**
```
STATE → INTENT → ACTION
```

### **5.2 Request → Response**
```
STATE → INTENT
INTENT → ACTION
ACTION → TRACE
```

### **5.3 Reasoning Chain**
```
STATE → PLAN → TRACE
```

### **5.4 Multi‑Agent Exchange**
```
STATE(A) → INTENT(B)
INTENT(B) → ACTION(A)
```

### **5.5 Error Recovery**
```
ANY → ERROR → STATE
```

These patterns define valid transitions between message types.

---

## **6. Validation Rules**

Validation ensures structural correctness and protocol compliance.

### **6.1 Packet Validation**
- `type` must be one of the six message types  
- `payload` must exist  
- `payload` must be a valid SUBIT sequence  
- `meta` is optional  

### **6.2 SUBIT Validation**
- bit length divisible by 6  
- each 6‑bit segment decodes to a valid form  
- INTENT, ACTION, PLAN require ≥12 bits  

### **6.3 Dialogue Validation**
- STATE cannot respond to ACTION  
- ERROR may respond to any message  
- TRACE may terminate any chain  
- PLAN must contain ≥2 transitions  

---

## **7. Interpretation Rules**

Agents interpret messages structurally:

- **STATE** — internal configuration  
- **INTENT** — desired transition or goal  
- **ACTION** — executable step  
- **PLAN** — multi‑step reasoning  
- **TRACE** — explanation or log  
- **ERROR** — structural failure  

Interpretation is deterministic and reversible through SUBIT‑Lingua encoding.

---

## **8. Examples**

### **8.1 Basic Exchange**
```
STATE:
000110

INTENT:
000110110001
```

### **8.2 Intent → Action**
```
INTENT:
011011000100

ACTION:
011011110001
```

### **8.3 Plan**
```
000110 110001 011011
```

### **8.4 Error**
```
ERROR:
111111
```

---

## **9. Reference Implementation**

The `src/` directory provides minimal tools:

- `encoder.py` — SUBIT encoding  
- `decoder.py` — SUBIT decoding  
- `validator.py` — packet validation  
- `agent.py` — minimal agent implementing the protocol  

These components form a baseline for integrating the protocol into agent systems.

---

## **10. Summary**

SUBIT‑Agent Protocol v1.0 defines:

- a unified packet format  
- six structural message types  
- deterministic dialogue patterns  
- strict validation rules  
- structural interpretation logic  
- examples and reference tools  

The protocol is compact, formal, and fully aligned with SUBIT‑Lingua v3.0.

---
