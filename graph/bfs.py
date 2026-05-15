from structures.graph import Graph
from collections import deque

# returns traversal order of the nodes
def bfs(graph: Graph, start: str):
    q = deque([start])
    visited = {start}
    order = []

    while q:
        cur_node = q.popleft()
        order.append(cur_node)

        yield {
            "current": cur_node,
            "visited": visited.copy(),
            "queue": list(q),
            "order": order.copy(),
        }

        for neighbor in graph.neighbors(cur_node):
            nei, _ = neighbor # bfs doesnt use weights
            if nei not in visited:
                visited.add(nei)
                q.append(nei)


"""
yield:
    - yield transforms a standard function into a generator, allowing it to produce a sequence of values over time rather than all at once.
      when python hits a yield statement, it "pauses" the function, saves its entire state, and returns a value to the caller.
"""