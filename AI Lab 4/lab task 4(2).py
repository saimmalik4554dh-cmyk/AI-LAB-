import heapq

graph = {
    'S': [('A', 3), ('D', 2)],
    'A': [('B', 5), ('C', 10)],
    'D': [('B', 1), ('E', 4)],
    'B': [('C', 2), ('E', 1)],
    'C': [('G', 4)],
    'E': [('G', 3)],
    'G': []
}

h = {'S': 7, 'A': 9, 'B': 4, 'C': 2,
     'D': 5, 'E': 3, 'G': 0}

def search(heuristic):
    q = [(heuristic['S'], 0, 0, 'S')]
    best = {'S': 0}
    order = {'S': 0}
    parent = {'S': None}
    closed = set()
    processed = []
    serial = 1
    stale = 0

    while q:
        f, seq, g, node = heapq.heappop(q)

        if g != best[node] or node in closed:
            stale += 1
            continue

        processed.append(node)
        closed.add(node)

        if node == 'G':
            break

        for nxt, cost in graph[node]:
            ng = g + cost

            if nxt not in closed and ng < best.get(nxt, float('inf')):
                best[nxt] = ng
                parent[nxt] = node

                if nxt not in order:
                    order[nxt] = serial
                    serial += 1

                heapq.heappush(
                    q, (ng + heuristic[nxt], order[nxt], ng, nxt)
                )

    path = []
    node = 'G'
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()

    check = sum(
        next(w for v, w in graph[u] if v == n)
        for u, n in zip(path, path[1:])
    )

    return path, check, processed, stale, sum(
        1 for _, _, g, n in q if g != best.get(n)
    )


for name, heuristic in [
    ("A*", h),
    ("UCS", {n: 0 for n in graph})
]:
    path, cost, processed, stale, pending = search(heuristic)

    print("\n", name)
    print("Path:", path)
    print("Path Cost:", cost)
    print("Verified Cost:", cost)
    print("Processed:", processed)
    print("Expansion Count:", len(processed) - 1)
    print("Stale Skipped:", stale)
    print("Stale Pending:", pending)