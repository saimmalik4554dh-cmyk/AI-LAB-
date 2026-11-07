g = {
'A':['B','C'], 'B':['A','D','E'],
'C':['A','F'], 'D':['B'], 'E':['B','F'],
'F':['C','E','G'], 'G':['F']
}

def dls(n, goal, limit, path):
    if n == goal:
        return "FOUND", path
    if len(path)-1 == limit:
        return "CUTOFF", None

    cutoff = False
    for x in g[n]:
        if x not in path:
            s, p = dls(x, goal, limit, path+[x])
            if s == "FOUND":
                return s, p
            if s == "CUTOFF":
                cutoff = True
    return ("CUTOFF", None) if cutoff else ("FAILURE", None)

def iddfs(maximum):
    for i in range(maximum+1):
        s, p = dls('A', 'G', i, ['A'])
        if s != "CUTOFF":
            return s, p, list(range(i+1))
    return "CUTOFF", None, list(range(maximum+1))

for i in range(1, 5):
    print("DLS", i, dls('A','G',i,['A']))
    print("IDDFS", i, iddfs(i))