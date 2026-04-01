from __future__ import annotations

from dataclasses import dataclass, field

from .clarification import ClarificationRouter
from .policy_graph import PolicyGraph
from .types import CaseInput, Decision, DecisionType, ExperienceRecord, TraceEvent


@dataclass(slots=True)
class HarnessRuntime:
    graph: PolicyGraph
    clarifier: ClarificationRouter
    trace: list[TraceEvent] = field(default_factory=list)

    def run_step(self, case: CaseInput, node_id: str | None = None) -> Decision:
        current_node_id = node_id or self.graph.start_node
        node = self.graph.get_node(current_node_id)

        if node.escalate_on_high_risk and case.risk_level == "high":
            decision = Decision(
                decision_type=DecisionType.ESCALATE,
                target="human_agent",
                reason="High risk case requires escalation.",
            )
            self._log(case.case_id, current_node_id, decision)
            return decision

        clarification = self.clarifier.decide(case, node)
        if clarification is not None:
            self._log(case.case_id, current_node_id, clarification)
            return clarification

        action = node.allowed_actions[0] if node.allowed_actions else "complete"
        decision_type = DecisionType.COMPLETE if current_node_id == "complete" or action == "complete" else DecisionType.ACTION
        decision = Decision(
            decision_type=decision_type,
            target=action,
            reason=f"Node '{current_node_id}' is ready for execution.",
        )
        self._log(case.case_id, current_node_id, decision)
        return decision

    def summarize_experience(self, case: CaseInput, success: bool, notes: str = "") -> ExperienceRecord:
        return ExperienceRecord(
            case_id=case.case_id,
            scene=case.current_state,
            final_outcome=self.trace[-1].decision_type if self.trace else "UNKNOWN",
            success=success,
            notes=notes,
        )

    def _log(self, case_id: str, node_id: str, decision: Decision) -> None:
        self.trace.append(
            TraceEvent(
                case_id=case_id,
                step_id=len(self.trace) + 1,
                node_id=node_id,
                decision_type=decision.decision_type.value,
                target=decision.target,
                reason=decision.reason,
            )
        )
