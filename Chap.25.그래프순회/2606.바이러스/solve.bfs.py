def bfs(v, G, mark):
    queue = []
    queue.append(v)
    mark[v] = True
    while len(queue) > 0:
        v = queue.pop(0)
        for u in G[v]:
            if not mark[u]:
                queue.append(u)
                mark[u] = True
    
def solve(n, G):
    mark = [False] * (n + 1)
    bfs(1, G, mark)
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