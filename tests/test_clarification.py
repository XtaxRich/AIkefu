from aikefu import CaseInput, ClarificationRouter, HarnessRuntime, PolicyGraph
from aikefu.types import DecisionType


def test_clarification_triggers_when_required_slot_missing() -> None:
    graph = PolicyGraph.demo_graph()
    runtime = HarnessRuntime(graph=graph, clarifier=ClarificationRouter())
    case = CaseInput(case_id="case-1", user_utterance="师傅怎么还没来", slots={"order_id": "o-1"})

    decision = runtime.run_step(case)

    assert decision.decision_type == DecisionType.CLARIFY
    assert "service_time" in decision.missing_slots
