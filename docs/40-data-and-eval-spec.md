# 40 Data and Eval Spec

## Core objects
### Case Input
- case_id
- scene
- user_utterance
- slots
- current_state
- risk_level

### Decision
- decision_type
- target
- reason
- missing_slots

### Trace Event
- case_id
- step_id
- node_id
- decision_type
- target
- reason
- timestamp

### Experience Record
- case_id
- scene
- final_outcome
- success
- error_type
- notes

## Core metrics
- policy_adherence
- required_step_coverage
- clarification_usefulness
- action_order_correctness
- escalation_correctness
- recovery_success
- cost_per_success_case

## Eval rule
Do not score only the final answer.
Score the full trace for each case.

## Required outputs for future code
- structured decision
- full trace
- replay support
- metrics mapping
- experience export
