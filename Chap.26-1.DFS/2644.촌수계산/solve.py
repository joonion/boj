def dfs(s, t, G, V):
    V[s] = 1
    if s == t:
        return 0
    else:
        minv = 10**6
        for u in G[s]:
            if not V[u]:
                minv = min(minv, dfs(u, t, G, V))
        return minv + 1

N, M = map(int, input().split())
P, Q = map(int, input().split())
G = {i:[] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
V = [0] * (N + 1)
print(dfs(P, Q, G, V))
