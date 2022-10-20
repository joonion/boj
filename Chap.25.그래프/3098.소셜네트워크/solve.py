def solve(n, G):
    for i in range(1, n + 1):
        for j in G[i]:
            for k in G[j]:
                if k not in G[i]:
                    G[i].append(k)
    
N, M = map(int, input().split())
G = {i:[] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    G[a], G[b] = b, a
    solve(N, G)