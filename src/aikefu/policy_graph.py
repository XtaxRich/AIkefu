from __future__ import annotations

from dataclasses import dataclass, field

from .types import PolicyNode


@dataclass(slots=True)
class PolicyGraph:
    nodes: dict[str, PolicyNode] = field(default_factory=dict)
    start_node: str = "root"

    def add_node(self, node: PolicyNode) -> None:
        self.nodes[node.node_id] = node

    def get_node(self, node_id: str) -> PolicyNode:
        if node_id not in self.nodes:
            raise KeyError(f"Unknown node: {node_id}")
        return self.nodes[node_id]

    def validate(self) -> None:
        if self.start_node not in self.nodes:
            raise ValueError(f"Start node '{self.start_node}' not found")
        for node in self.nodes.values():
            for _, next_node in node.next_nodes.items():
                if next_node not in self.nodes:
                    raise ValueError(f"Node '{node.node_id}' points to missing node '{next_node}'")

    @classmethod
    def demo_graph(cls) -> "PolicyGraph":
        graph = cls(start_node="fulfillment_check")
        graph.add_node(
            PolicyNode(
                node_id="fulfillment_check",
                required_slots=["order_id", "service_time"],
                allowed_actions=["query_order", "query_master_status"],
                next_nodes={"clarified": "decision", "ready": "decision"},
            )
        )
        graph.add_node(
            PolicyNode(
                node_id="decision",
                required_slots=["order_id", "service_time", "contact_status"],
                allowed_actions=["notify_user", "call_master", "escalate"],
                next_nodes={"done": "complete"},
                escalate_on_high_risk=True,
            )
        )
        graph.add_node(PolicyNode(node_id="complete"))
        graph.validate()
        return graph
