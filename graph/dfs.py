from structures.graph import Graph

def dfs(graph: Graph, start: str):
    stack = [start]
    visited = set()
    order = []

    while stack:
        cur_node = stack.pop()

        if cur_node in visited:
            continue

        visited.add(cur_node)
        order.append(cur_node)

        yield {
            "current": cur_node,
            "visited": visited.copy(),
            "stack": stack,
            "order": order.copy(),
        }

        for neighbor in graph.neighbors(cur_node):
            nei, _ = neighbor 
            if nei not in visited:
                stack.append(nei)


"""
*iterative DFS usually mark nodes visited when popping from the stack (both work though, i just chose when popping because
it looks better on the visualizer), whereas BFS usually marks when enqueueing.
"""