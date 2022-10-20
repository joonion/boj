def dfs(v, G, mark):
    mark[v] = True
    for u in G[v]:
        if not mark[u]:
            dfs(u, G, mark)
    
def solve(n, G):
    mark = [False] * (n + 1)
    dfs(1, G, mark)
    return sum(mark) - 1

N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
answer = solve(N, G)
print(answer)