"""
LLM assisted code
"""
from pyvis.network import Network


class GraphVisualizer:
    def __init__(self, height="700px", width="100%"):
        self.height = height
        self.width = width

    def build_network(self, graph, state=None):
        net = Network(
            height=self.height,
            width=self.width,
            directed=graph.directed
        )

        state = state or {}

        current = state.get("current")
        visited = state.get("visited", set())
        queue = state.get("queue", [])

        for node_name in graph.nodes:
            color = "lightgray"

            if node_name in visited:
                color = "lightgreen"

            if node_name in queue:
                color = "lightblue"

            if node_name == current:
                color = "yellow"

            net.add_node(node_name, label=node_name, color=color)

        for edge in graph.get_edges():
            net.add_edge(
                edge.src,
                edge.dist,
                label=str(edge.weight)
            )

        return net

    def render(self, graph, state=None, output_file="graph.html"):
        net = self.build_network(graph, state)
        net.write_html(output_file)

    def render_to_html(self, graph, state=None):
        net = self.build_network(graph, state)
        return net.generate_html()