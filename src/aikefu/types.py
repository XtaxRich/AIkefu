from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class DecisionType(str, Enum):
    CLARIFY = "CLARIFY"
    ACTION = "ACTION"
    ESCALATE = "ESCALATE"
    COMPLETE = "COMPLETE"


@dataclass(slots=True)
class CaseInput:
    case_id: str
    user_utterance: str
    slots: dict[str, str] = field(default_factory=dict)
    current_state: str = "unknown"
    risk_level: str = "medium"


@dataclass(slots=True)
class PolicyNode:
    node_id: str
    required_slots: list[str] = field(default_factory=list)
    allowed_actions: list[str] = field(default_factory=list)
    next_nodes: dict[str, str] = field(default_factory=dict)
    escalate_on_high_risk: bool = False


@dataclass(slots=True)
class Decision:
    decision_type: DecisionType
    target: str
    reason: str
    missing_slots: list[str] = field(default_factory=list)


@dataclass(slots=True)
class TraceEvent:
    case_id: str
    step_id: int
    node_id: str
    decision_type: str
    target: str
    reason: str


@dataclass(slots=True)
class ExperienceRecord:
    case_id: str
    scene: str
    final_outcome: str
    success: bool
    notes: str = ""
