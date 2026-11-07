from heapq import heappush, heappop
from collections import deque

edges = [('A','B',1), ('A','C',5), ('B','D',2),
         ('B','E',1), ('C','F',5), ('E','F',1), ('F','G',1)]

g = {n: [] for n in "ABCDEFG"}
for u, v, w in edges:
    g[u].append((v,w))
    g[v].append((u,w))

def ucs():
    q = [(0,'A',['A'])]
    best = {'A': 0}
    order = []
    while q:
        c, n, p = heappop(q)
        if c != best[n]:
            continue
        order.append(n)
        if n == 'G':
            return p, c, order
        for v, w in g[n]:
            nc = c + w
            if nc < best.get(v, 999):
                best[v] = nc
                heappush(q, (nc,v,p+[v]))

def bfs():
    q = deque([('A',['A'])])
    seen = {'A'}
    order = []
    while q:
        n, p = q.popleft()
        order.append(n)
        if n == 'G':
            return p, order
        for v, w in g[n]:
            if v not in seen:
                seen.add(v)
                q.append((v,p+[v]))

p, c, order = ucs()
bp, bo = bfs()

cost = lambda path: sum(
    next(w for v,w in g[u] if v == x)
    for u,x in zip(path,path[1:])
)

print("UCS:", order, p, c)
print("Verified Cost:", cost(p))
print("BFS:", bo, bp, cost(bp))