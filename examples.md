# **examples.md**  
### **SUBIT‑Agent Protocol v1.0 — Examples**

These examples demonstrate how SUBIT‑encoded packets form valid dialogues within the protocol.  
All payloads are SUBIT sequences; all dialogues follow the structural rules defined in the specification.

---

## **1. Basic Decision Cycle**

A minimal STATE → INTENT → ACTION flow.

### Packets
```
STATE
000110
```

```
INTENT
000110110001
```

```
ACTION
011011110001
```

### Interpretation
- STATE sets the agent’s configuration.  
- INTENT expresses a desired transition.  
- ACTION executes the transition.

---

## **2. Request → Response Pattern**

A simple query‑response with reasoning.

### Packets
```
STATE
010101
```

```
INTENT
010101001111
```

```
ACTION
001111011000
```

```
TRACE
001111011000011011
```

### Interpretation
- The agent receives context.  
- It generates intent.  
- It performs the action.  
- It returns a reasoning trace.

---

## **3. Multi‑Step Reasoning (PLAN → TRACE)**

A structured reasoning chain.

### Packets
```
STATE
000010
```

```
PLAN
000010 110001 011011 010100
```

```
TRACE
110001 011011 010100
```

### Interpretation
- PLAN encodes a multi‑step transformation.  
- TRACE explains the reasoning.

---

## **4. Multi‑Agent Exchange**

Two agents coordinating.

### Agent A → Agent B
```
STATE(A)
000110
```

### Agent B → Agent A
```
INTENT(B)
000110110001
```

### Agent A → Agent B
```
ACTION(A)
110001011000
```

### Interpretation
- A provides context.  
- B generates intent.  
- A executes the action.

---

## **5. Error Recovery**

A dialogue with structural failure and reset.

### Packets
```
STATE
001100
```

```
INTENT
001100111000
```

```
ERROR
111111
```

```
STATE
010000
```

```
INTENT
010000110001
```

```
ACTION
110001011011
```

### Interpretation
- ERROR invalidates the previous chain.  
- A new STATE resets the dialogue.  
- The cycle continues normally.

---

## **6. Extended Reasoning Loop**

A longer reasoning cycle combining planning and execution.

### Packets
```
STATE
000001
```

```
PLAN
000001 000111 001111 011111
```

```
ACTION
011111010101
```

```
TRACE
000111 001111 011111
```

### Interpretation
- PLAN defines the reasoning path.  
- ACTION executes the final step.  
- TRACE provides explanation.

---

## **7. Minimal Valid Packets**

### STATE
```
{
  "type": "STATE",
  "payload": "000110"
}
```

### INTENT
```
{
  "type": "INTENT",
  "payload": "000110110001"
}
```

### ACTION
```
{
  "type": "ACTION",
  "payload": "011011110001"
}
```

### PLAN
```
{
  "type": "PLAN",
  "payload": "000110110001011011"
}
```

### TRACE
```
{
  "type": "TRACE",
  "payload": "110001011011"
}
```

### ERROR
```
{
  "type": "ERROR",
  "payload": "111111"
}
```

---

## **8. Invalid Dialogue Examples**

### Missing initial STATE
```
INTENT → ACTION
```

### Illegal transition
```
ACTION → STATE
```

### Backwards reasoning
```
PLAN → INTENT
```

These violate the dialogue rules and must produce an ERROR.

---
