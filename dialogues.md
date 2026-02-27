# **dialogues.md**  
### **SUBIT‑Agent Protocol v1.0 — Dialogue Patterns**

Dialogue patterns define how SUBIT‑encoded packets combine into coherent interaction flows.  
Each pattern is deterministic, minimal, and built from the six message types: STATE, INTENT, ACTION, PLAN, TRACE, ERROR.

All patterns operate on SUBIT sequences and follow the packet rules defined in the protocol specification.

---

## **1. State → Intent → Action**

This is the core structural dialogue pattern.  
It represents a complete decision cycle from context to goal to execution.

```
STATE → INTENT → ACTION
```

- **STATE** provides the initial configuration.  
- **INTENT** expresses the desired transition.  
- **ACTION** executes the transition.

**Example:**
```
STATE: 000110
INTENT: 000110110001
ACTION: 011011110001
```

---

## **2. Request → Response**

A general-purpose exchange used for queries, commands, and simple tasks.

```
STATE → INTENT
INTENT → ACTION
ACTION → TRACE
```

- The agent receives context (STATE).  
- It responds with a goal (INTENT).  
- It performs the operation (ACTION).  
- It optionally returns reasoning (TRACE).

---

## **3. Reasoning Chain**

Used when an agent must compute a multi-step transformation or explanation.

```
STATE → PLAN → TRACE
```

- **PLAN** encodes a structured sequence of transitions.  
- **TRACE** provides the final reasoning log.

**Example:**
```
PLAN: 000110 110001 011011
TRACE: 110001 011011 011111
```

---

## **4. Multi‑Agent Exchange**

Two agents coordinate by alternating STATE, INTENT, and ACTION messages.

```
STATE(A) → INTENT(B)
INTENT(B) → ACTION(A)
```

- Agent A provides context.  
- Agent B generates intent.  
- Agent A executes the action.

This pattern generalizes to N agents by chaining STATE and INTENT messages.

---

## **5. Error Recovery**

Errors are structural and must be resolved deterministically.

```
ANY → ERROR → STATE
```

- Any invalid message or transition produces an ERROR.  
- The next valid message must be a new STATE.  
- This resets the dialogue.

**Example:**
```
ERROR: 111111
STATE: 000010
```

---

## **6. Extended Reasoning Loop**

A longer reasoning cycle combining planning and execution.

```
STATE
→ PLAN
→ ACTION
→ TRACE
```

- PLAN defines the reasoning path.  
- ACTION executes the final step.  
- TRACE explains the process.

---

## **7. Negotiation Pattern**

Two agents converge on a shared intent.

```
STATE(A) → INTENT(A)
STATE(B) → INTENT(B)
INTENT(A) ↔ INTENT(B)
→ ACTION
```

- Both agents express their intents.  
- They exchange transitions until convergence.  
- A final ACTION resolves the negotiation.

---

## **8. Dialogue Validity Rules**

A dialogue is valid if:

- It begins with **STATE**.  
- It ends with **ACTION**, **TRACE**, or **ERROR**.  
- No ACTION precedes INTENT.  
- No INTENT precedes STATE.  
- TRACE may follow any message.  
- ERROR resets the dialogue.  

These rules ensure deterministic interpretation.

---

## **9. Minimal Examples**

### **Simple Task**
```
STATE
INTENT
ACTION
```

### **Reasoning with Explanation**
```
STATE
PLAN
TRACE
```

### **Error Handling**
```
STATE
INTENT
ERROR
STATE
INTENT
ACTION
```

---

Here is **dialogues.md** — compact, structural, and fully aligned with the SUBIT‑Agent Protocol architecture.  
It defines the canonical interaction patterns between agents using SUBIT‑encoded messages.

---

# **dialogues.md**  
### **SUBIT‑Agent Protocol v1.0 — Dialogue Patterns**

Dialogue patterns define how SUBIT‑encoded packets combine into coherent interaction flows.  
Each pattern is deterministic, minimal, and built from the six message types: STATE, INTENT, ACTION, PLAN, TRACE, ERROR.

All patterns operate on SUBIT sequences and follow the packet rules defined in the protocol specification.

---

## **1. State → Intent → Action**

This is the core structural dialogue pattern.  
It represents a complete decision cycle from context to goal to execution.

```
STATE → INTENT → ACTION
```

- **STATE** provides the initial configuration.  
- **INTENT** expresses the desired transition.  
- **ACTION** executes the transition.

**Example:**
```
STATE: 000110
INTENT: 000110110001
ACTION: 011011110001
```

---

## **2. Request → Response**

A general-purpose exchange used for queries, commands, and simple tasks.

```
STATE → INTENT
INTENT → ACTION
ACTION → TRACE
```

- The agent receives context (STATE).  
- It responds with a goal (INTENT).  
- It performs the operation (ACTION).  
- It optionally returns reasoning (TRACE).

---

## **3. Reasoning Chain**

Used when an agent must compute a multi-step transformation or explanation.

```
STATE → PLAN → TRACE
```

- **PLAN** encodes a structured sequence of transitions.  
- **TRACE** provides the final reasoning log.

**Example:**
```
PLAN: 000110 110001 011011
TRACE: 110001 011011 011111
```

---

## **4. Multi‑Agent Exchange**

Two agents coordinate by alternating STATE, INTENT, and ACTION messages.

```
STATE(A) → INTENT(B)
INTENT(B) → ACTION(A)
```

- Agent A provides context.  
- Agent B generates intent.  
- Agent A executes the action.

This pattern generalizes to N agents by chaining STATE and INTENT messages.

---

## **5. Error Recovery**

Errors are structural and must be resolved deterministically.

```
ANY → ERROR → STATE
```

- Any invalid message or transition produces an ERROR.  
- The next valid message must be a new STATE.  
- This resets the dialogue.

**Example:**
```
ERROR: 111111
STATE: 000010
```

---

## **6. Extended Reasoning Loop**

A longer reasoning cycle combining planning and execution.

```
STATE
→ PLAN
→ ACTION
→ TRACE
```

- PLAN defines the reasoning path.  
- ACTION executes the final step.  
- TRACE explains the process.

---

## **7. Negotiation Pattern**

Two agents converge on a shared intent.

```
STATE(A) → INTENT(A)
STATE(B) → INTENT(B)
INTENT(A) ↔ INTENT(B)
→ ACTION
```

- Both agents express their intents.  
- They exchange transitions until convergence.  
- A final ACTION resolves the negotiation.

---

## **8. Dialogue Validity Rules**

A dialogue is valid if:

- It begins with **STATE**.  
- It ends with **ACTION**, **TRACE**, or **ERROR**.  
- No ACTION precedes INTENT.  
- No INTENT precedes STATE.  
- TRACE may follow any message.  
- ERROR resets the dialogue.  

These rules ensure deterministic interpretation.

---

## **9. Minimal Examples**

### **Simple Task**
```
STATE
INTENT
ACTION
```

### **Reasoning with Explanation**
```
STATE
PLAN
TRACE
```

### **Error Handling**
```
STATE
INTENT
ERROR
STATE
INTENT
ACTION
```

---
