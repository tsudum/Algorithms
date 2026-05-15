from dataclasses import dataclass

@dataclass
class Edge:
    src: str
    dist: str
    weight: float = 1