import heapq

graph = {
    'S': [('A',3), ('D',2)],
    'A': [('B',5), ('C',10)],
    'D': [('B',1), ('E',4)],
    'B': [('C',2), ('E',1)],
    'C': [('G',4)],
    'E': [('G',3)],
    'G': []
}

h = {'S':7, 'A':9, 'B':4, 'C':2,
     'D':5, 'E':3, 'G':0}

def astar(h):
    q = [(h['S'], 0, 'S', 0)]
    best = {'S':0}
    parent = {'S':None}
    closed = set()
    order = 1
    visited = []

    while q:
        f, _, node, g = heapq.heappop(q)

        if g != best[node] or node in closed:
            continue

        visited.append(node)
        closed.add(node)

        if node == 'G':
            break

        for v, w in graph[node]:
            ng = g + w
            if v not in closed and ng < best.get(v, 999):
                best[v] = ng
                parent[v] = node
                heapq.heappush(q, (ng+h[v], order, v, ng))
                order += 1

    path = []
    n = 'G'
    while n is not None:
        path.append(n)
        n = parent[n]
    path.reverse()

    cost = sum(
        next(w for v, w in graph[u] if v == x)
        for u, x in zip(path, path[1:])
    )

    return path, cost, visited


original = h.copy()
modified = h.copy()
modified['C'] = 10

print("Original Heuristic:", original['C'])
print("Modified Heuristic:", modified['C'])
print("True Cost from C to G: 4")

print("\nOriginal A*:")
print(astar(original))

print("\nModified A*:")
print(astar(modified))