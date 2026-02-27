# **validation.md**  
### **SUBIT‑Agent Protocol v1.0 — Validation Rules**

Validation ensures that every packet, payload, and dialogue in the SUBIT‑Agent Protocol is structurally correct, SUBIT‑valid, and compliant with the protocol’s interaction rules.  
All validation is deterministic and based solely on SUBIT‑Lingua structure and protocol constraints.

---

## **1. Packet Validation**

A packet is valid if it satisfies all of the following:

### **1.1 Required fields**
- `type` must exist  
- `payload` must exist  
- `type` must be one of:  
  `STATE`, `INTENT`, `ACTION`, `PLAN`, `TRACE`, `ERROR`  

### **1.2 Payload format**
- payload must be a SUBIT sequence  
- bit length divisible by 6  
- no invalid characters or malformed segments  

### **1.3 Metadata**
- `meta` is optional  
- if present, it must be a JSON object  
- metadata does not affect structural validity  

---

## **2. SUBIT Validation**

Payloads must be valid SUBIT‑Lingua sequences.

### **2.1 Form validation**
- exactly 6 bits  
- must decode to a valid SUBIT form index (0–63)

### **2.2 Transition validation**
- exactly 12 bits  
- must decode to two valid forms  
- used for INTENT and ACTION

### **2.3 Sequence validation**
- length ≥ 6 bits  
- divisible by 6  
- each 6‑bit segment must decode to a valid form  
- PLAN requires ≥ 3 forms  
- TRACE requires ≥ 2 forms  

### **2.4 Error payloads**
- may be 1 form or 1 transition  
- must still be valid SUBIT sequences  

---

## **3. Message‑Type Validation**

Each message type has structural constraints:

### **STATE**
- payload = 1 form (6 bits)

### **INTENT**
- payload = 1 transition or short sequence  
- minimum 12 bits

### **ACTION**
- payload = 1 transition  
- exactly 12 bits

### **PLAN**
- payload = sequence of ≥ 3 forms  
- minimum 18 bits

### **TRACE**
- payload = sequence of ≥ 2 forms  
- minimum 12 bits

### **ERROR**
- payload = 1 form or 1 transition  
- minimum 6 bits  

---

## **4. Dialogue Validation**

Dialogue validation ensures that message sequences follow protocol rules.

### **4.1 Start rules**
- every dialogue must begin with `STATE`  
- `STATE` cannot appear after `ACTION` or `PLAN` unless preceded by `ERROR`

### **4.2 Transition rules**
- `STATE → INTENT` is valid  
- `INTENT → ACTION` is valid  
- `STATE → PLAN` is valid  
- `PLAN → TRACE` is valid  
- `ACTION → TRACE` is valid  

### **4.3 Forbidden transitions**
- `ACTION → INTENT`  
- `ACTION → STATE`  
- `INTENT → STATE`  
- `TRACE → INTENT`  
- `TRACE → ACTION`  

### **4.4 Error rules**
- `ANY → ERROR` is valid  
- after `ERROR`, the next message must be `STATE`  
- `ERROR` may terminate a dialogue  

### **4.5 Termination rules**
A dialogue may end with:
- `ACTION`  
- `TRACE`  
- `ERROR`  

---

## **5. Structural Consistency Checks**

A packet or dialogue is invalid if:

- payload contains malformed SUBIT segments  
- bit length is not divisible by 6  
- message type does not match payload structure  
- dialogue violates ordering rules  
- PLAN or TRACE is too short  
- ERROR is followed by anything except STATE  

---

## **6. Minimal Examples**

### **Valid**
```
STATE → INTENT → ACTION
```

### **Valid with reasoning**
```
STATE → PLAN → TRACE
```

### **Valid with error recovery**
```
STATE → INTENT → ERROR → STATE → INTENT → ACTION
```

### **Invalid**
```
INTENT → ACTION
```
(no initial STATE)

```
ACTION → STATE
```
(illegal transition)

```
PLAN → INTENT
```
(backwards transition)

---
