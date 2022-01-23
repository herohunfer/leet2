class GraphNode:
    def __init__(self, value: int, successors: list):
        self.value = value
        self.successors = successors

def bipartite(graph: list):
    visited = {}
    for i in range(len(graph)):
        if not bfs(i, visited, graph):
            return False
    return True

def bfs(pos: int, visited: dict, graph: list):
    if pos in visited:
        return True
    q = [pos]
    visited[pos] = 0
    while len(q):
        current = q.pop()
        currentGroup = visited[current]
        neighborGroup = 0 if currentGroup == 1 else 1
        for nei in graph[current].successors:
            if nei not in visited:
                visited[nei] = neighborGroup
                q.append(nei)
            elif visited[nei] == currentGroup:
                return False
    return True

if __name__ == "__main__":

    nodes = [GraphNode(1, []), GraphNode(2, []), GraphNode(3, []), GraphNode(4, [])]
    nodes[0].successors = [1,2]
    nodes[1].successors = [0]
    nodes[2].successors = [0,3]
    nodes[3].successors = [2]
    print(bipartite(nodes))
