import sys
input = sys.stdin.readline

def bfs(v, G, D):
    mark = [[False] * len(D) for _ in range(len(D))]
    queue = []
    queue.append(v)
    mark[v] = True
    while len(queue) > 0:
        v = queue.pop(0)
        for u in G[v]:
            if not mark[u]:
                queue.append(u)
                mark[u] = True

def solve():
    n, m = map(int, input().split())
    G = {i:[] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, input().split())
        if v not in G[u]:
            G[u].append(v)
        if u not in G[v]:
            G[v].append(u)
    D = [[0] * (n + 1) for _ in range(n + 1)]
    bfs(1, G, D)
    minbacon, minv = n ** n, 0
    for v in range(1, n + 1):
        nbacon = sum(D[v])
        if nbacon < minbacon:
            nbacon, minv = minbacon, minv
    print(minv)

solve()
    