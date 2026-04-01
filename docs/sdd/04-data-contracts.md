# 04 Data Contracts

## CaseInput
- case_id: str
- user_utterance: str
- slots: dict[str, str]
- current_state: str
- risk_level: str

## Decision
- decision_type: CLARIFY | ACTION | ESCALATE | COMPLETE
- target: str
- reason: str
- missing_slots: list[str]

## TraceEvent
- case_id: str
- step_id: int
- node_id: str
- decision_type: str
- target: str
- reason: str

## ExperienceRecord
- case_id: str
- scene: str
- final_outcome: str
- success: bool
- notes: str
