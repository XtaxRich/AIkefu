from aikefu.policy_graph import PolicyGraph


def test_demo_graph_is_valid() -> None:
    graph = PolicyGraph.demo_graph()
    assert graph.start_node == "fulfillment_check"
    assert graph.get_node("decision").escalate_on_high_risk is True
