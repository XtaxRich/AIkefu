from __future__ import annotations

from .types import CaseInput, Decision, DecisionType, PolicyNode


class ClarificationRouter:
    """Minimal clarification-first router.

    The first stage is intentionally simple and deterministic.
    Later iterations can replace this module with a learned policy.
    """

    def missing_slots(self, case: CaseInput, node: PolicyNode) -> list[str]:
        return [slot for slot in node.required_slots if not case.slots.get(slot)]

    def decide(self, case: CaseInput, node: PolicyNode) -> Decision | None:
        missing = self.missing_slots(case, node)
        if not missing:
            return None
        return Decision(
            decision_type=DecisionType.CLARIFY,
            target=missing[0],
            reason=f"Missing required slot(s): {', '.join(missing)}",
            missing_slots=missing,
        )
