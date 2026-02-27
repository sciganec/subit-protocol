# **interpretation.md**  
### **SUBIT‑Agent Protocol v1.0 — Interpretation Model**

Interpretation is the process by which an agent transforms SUBIT‑encoded packets into internal state updates, decisions, actions, and reasoning outputs.  
The model is deterministic, reversible, and fully grounded in SUBIT‑Lingua structure.

---

## **1. Interpretation Pipeline**

Every packet passes through the same four‑stage pipeline:

1. **Decode** — convert SUBIT bitstream into forms, transitions, or sequences.  
2. **Classify** — identify the message type (STATE, INTENT, ACTION, PLAN, TRACE, ERROR).  
3. **Map** — apply structural rules to update internal state or generate outputs.  
4. **Respond** — produce the next packet according to dialogue rules.

This pipeline ensures consistent behavior across all agents.

---

## **2. STATE Interpretation**

A STATE packet defines the agent’s current configuration.

- The payload is a single SUBIT form.  
- The form is mapped to an internal state vector or configuration slot.  
- All subsequent interpretation depends on this state.

**Effect:**  
Updates the agent’s internal state baseline.

---

## **3. INTENT Interpretation**

An INTENT packet expresses a desired transition or goal.

- The payload is a transition (two forms) or short sequence.  
- The agent interprets the transition as a directional change from its current state.  
- The agent evaluates whether the transition is valid, achievable, or requires planning.

**Effect:**  
Generates an ACTION or PLAN depending on complexity.

---

## **4. ACTION Interpretation**

An ACTION packet represents an executable step.

- The payload is a single transition.  
- The agent interprets the transition as a direct operation.  
- Execution may modify internal state, external environment, or both.

**Effect:**  
Performs the operation and optionally produces a TRACE.

---

## **5. PLAN Interpretation**

A PLAN packet encodes a multi‑step reasoning chain.

- The payload is a sequence of ≥3 forms.  
- Each adjacent pair is interpreted as a transition.  
- The agent evaluates the sequence as a structured transformation path.

**Effect:**  
Executes or refines the plan, then produces TRACE or ACTION.

---

## **6. TRACE Interpretation**

A TRACE packet provides a reasoning log.

- The payload is a sequence of ≥2 forms.  
- The agent interprets it as an explanation of prior steps.  
- TRACE does not modify state; it finalizes the dialogue.

**Effect:**  
Completes the reasoning cycle.

---

## **7. ERROR Interpretation**

An ERROR packet signals structural or semantic failure.

- The payload is a form or short sequence.  
- The agent interprets it as a failure code.  
- The next valid message must be a new STATE.

**Effect:**  
Resets the dialogue.

---

## **8. Mapping Rules**

Interpretation relies on structural mapping:

- **Form → State**  
  A single form maps to an internal configuration.

- **Transition → Operation**  
  A pair of forms maps to a directional change or executable step.

- **Sequence → Reasoning**  
  A chain of forms maps to a structured transformation path.

These mappings are deterministic and reversible.

---

## **9. Dialogue‑Driven Interpretation**

Interpretation depends on dialogue context:

- After **STATE**, the agent expects INTENT or PLAN.  
- After **INTENT**, the agent expects ACTION or PLAN.  
- After **ACTION**, the agent may produce TRACE.  
- After **PLAN**, the agent may produce ACTION or TRACE.  
- After **ERROR**, the agent expects STATE.

Dialogue rules ensure predictable behavior.

---

## **10. Internal State Model**

Agents maintain:

- **current SUBIT form** (state)  
- **pending transition** (intent)  
- **execution context** (action)  
- **reasoning buffer** (plan/trace)  
- **error flag** (if needed)

Interpretation updates these components deterministically.

---

## **11. Example Interpretation Flow**

### Input:
```
STATE: 000110
INTENT: 000110110001
ACTION: 011011110001
TRACE: 110001011011
```

### Interpretation:
- STATE sets internal configuration.  
- INTENT defines desired transition.  
- ACTION executes the transition.  
- TRACE explains the reasoning.

### Result:
A complete, valid decision cycle.

---

## **12. Summary**

Interpretation in the SUBIT‑Agent Protocol:

- decodes SUBIT sequences  
- maps forms and transitions to internal state and behavior  
- follows deterministic dialogue rules  
- produces structured outputs (ACTION, PLAN, TRACE)  
- resets cleanly on ERROR  

This model ensures universal, predictable, interoperable agent behavior.

---
