# 40 Data and Eval Spec

## Core objects
### Case Input
- case_id
- user text
- known slots
- current state
- risk level

### Decision
- clarify
- action
- escalate
- complete

### Trace Event
- step id
- node id
- decision type
- target
- reason

### Experience Record
- case id
- scene
- final outcome
- success flag
- notes

## Core metrics
- policy adherence
- required-step coverage
- clarification usefulness
- action-order correctness
- escalation correctness
- recovery success
- cost per successful case

## Evaluation rule
Do not score only the final answer. Score the full trace.
