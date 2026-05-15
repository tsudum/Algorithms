from structures.node import Node
from structures.edge import Edge


class Graph:
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.nodes: dict[str, Node] = {}
        self.adjacency: dict[str, list[tuple[str, float]]] = {} # key: node name, value: list of (neighbor, weight)
        self.edges: list[Edge] = []

    # create nodes
    def add_node(self, name: str):
        if name not in self.nodes:
            self.nodes[name] = Node(name)
            self.adjacency[name] = []

    # connect nodes
    def add_edge(self, source: str, destination: str, weight: float = 1):
        self.add_node(source)
        self.add_node(destination)

        self.adjacency[source].append((destination, weight))
        self.edges.append(Edge(source, destination, weight))

        if not self.directed:
            self.adjacency[destination].append((source, weight))

    # get neighbors / traverse graph
    def neighbors(self, name: str) -> list[tuple[str, float]]:
        return self.adjacency[name]

    # return all edges of the graph
    def get_edges(self) -> list[Edge]:
        return self.edges