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

frontier = {'S': (0, 0)}
visited = set()
order = 1

for step in range(1, 4):
    node = min(frontier, key=lambda n:
               (frontier[n][0] + h[n], frontier[n][1]))

    g, pos = frontier.pop(node)
    visited.add(node)

    print("\nExpansion:", node)
    print("g =", g, "h =", h[node], "f =", g + h[node])

    for nxt, cost in graph[node]:
        new_g = g + cost

        if nxt in visited:
            continue

        if nxt not in frontier:
            frontier[nxt] = (new_g, order)
            order += 1
        elif new_g < frontier[nxt][0]:
            frontier[nxt] = (new_g, frontier[nxt][1])

    remaining = sorted(
        frontier,
        key=lambda n: (frontier[n][0] + h[n], frontier[n][1])
    )

    print("Frontier:", [
        (n, frontier[n][0], h[n], frontier[n][0] + h[n])
        for n in remaining
    ])