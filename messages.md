# **messages.md**  
### **SUBIT‑Agent Protocol v1.0 — Message Types**

SUBIT‑Agent Protocol defines six structural message types.  
Each message type is expressed as a SUBIT‑encoded payload wrapped in a protocol packet.

All payloads must be valid SUBIT sequences (bit length divisible by 6).

---

## **1. STATE**

Represents the agent’s current internal configuration.

- **Payload:** one SUBIT form (6 bits)  
- **Role:** provides context for intent generation  
- **Dialogue position:** always the first message in a chain  

**Example:**
```
STATE
000110
```

---

## **2. INTENT**

Represents a desired transition, goal, or direction of change.

- **Payload:** one SUBIT transition (12 bits) or short sequence  
- **Role:** expresses what the agent wants to do next  
- **Dialogue position:** follows STATE  

**Example:**
```
INTENT
000110110001
```

---

## **3. ACTION**

Represents an executable operation derived from intent.

- **Payload:** one SUBIT transition (12 bits)  
- **Role:** concrete step the agent will perform  
- **Dialogue position:** follows INTENT  

**Example:**
```
ACTION
011011110001
```

---

## **4. PLAN**

Represents a structured multi‑step reasoning chain.

- **Payload:** SUBIT sequence (≥ 3 forms)  
- **Role:** outlines a multi‑stage transformation or reasoning path  
- **Dialogue position:** may follow STATE or INTENT  

**Example:**
```
PLAN
000110 110001 011011
```

---

## **5. TRACE**

Represents an explanation or reasoning log.

- **Payload:** SUBIT sequence (any length ≥ 2 forms)  
- **Role:** provides transparency into the agent’s reasoning  
- **Dialogue position:** may terminate any chain  

**Example:**
```
TRACE
110001 011011 011111
```

---

## **6. ERROR**

Represents a structural or semantic failure.

- **Payload:** one form or short sequence  
- **Role:** signals invalid input, invalid transition, or protocol violation  
- **Dialogue position:** may follow any message type  

**Example:**
```
ERROR
111111
```

---

## **Message Summary Table**

| Type | Payload | Minimum Bits | Purpose | Typical Position |
|------|---------|--------------|---------|------------------|
| STATE | Form | 6 | Internal configuration | Start |
| INTENT | Transition / short sequence | 12 | Desired change | After STATE |
| ACTION | Transition | 12 | Executable step | After INTENT |
| PLAN | Sequence | 18 | Multi‑step reasoning | After STATE/INTENT |
| TRACE | Sequence | 12 | Explanation/log | End |
| ERROR | Form / short sequence | 6 | Failure signal | Anywhere |

---

## **Structural Constraints**

- All payloads must be valid SUBIT sequences.  
- Bit length must be divisible by 6.  
- INTENT and ACTION require at least 12 bits.  
- PLAN requires at least 18 bits (3 forms).  
- ERROR may be minimal (6 bits).  
- STATE cannot follow ACTION.  
- TRACE may follow any message.  

---

## **Minimal Packet Examples**

### STATE packet
```
{
  "type": "STATE",
  "payload": "000110"
}
```

### INTENT packet
```
{
  "type": "INTENT",
  "payload": "000110110001"
}
```

### ERROR packet
```
{
  "type": "ERROR",
  "payload": "111111"
}
```

---
