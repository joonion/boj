def dfs(v, G, visited):
    visited[v] = True
    print(v, end = " ")
    for u in G[v]:
        if not visited[u]:
            dfs(u, G, visited)

def bfs(v, G):
    queue = []
    visited = [False] * len(G)
    queue.append(v)
    visited[v] = True
    print(v, end = " ")
    while len(queue) > 0:
        v = queue.pop(0)
        for u in G[v]:
            if not visited[u]:
                queue.append(u)
                visited[u] = True
                print(u, end = " ")

import sys
input = sys.stdin.readline
N, M, V = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
for v in range(N + 1):
    G[v].sort()

visited = [False] * len(G)
dfs(V, G, visited)
print()
bfs(V, G)
