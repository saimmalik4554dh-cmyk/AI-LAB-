from collections import deque

def bfs(g, start, goal):
    q = deque([(start, [start])])
    seen = {start}
    while q:
        n, p = q.popleft()
        if n == goal:
            return p
        for x in g[n]:
            if x not in seen:
                seen.add(x)
                q.append((x, p + [x]))

def dfs(g, start, goal):
    stack = [(start, [start])]
    seen = set()
    while stack:
        n, p = stack.pop()
        if n in seen:
            continue
        seen.add(n)
        if n == goal:
            return p
        for x in reversed(g[n]):
            if x not in seen:
                stack.append((x, p + [x]))

print("BFS Path:", bfs(graph, 'A', 'G'))
print("DFS Path:", dfs(graph, 'A', 'G'))