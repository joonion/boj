def bfs(r, n, G, T):
    Q = []
    Q.append(r)
    mark = [False] * (n + 1)
    mark[r] = True
    while len(Q) > 0:
        v = Q.pop(0)
        for u in G[v]:
            if not mark[u]:
                mark[u] = True
                Q.append(u)
                T[u] = v
                
def solve(n, A):
    G = {i:[] for i in range(1, n + 1)}
    for e in A:
        G[e[0]].append(e[1])
        G[e[1]].append(e[0])
    T = [0] * (n + 1)
    bfs(1, n, G, T)
    for i in range(2, n + 1):
        print(T[i])
    
n = int(input())
A = [list(map(int, input().split())) for _ in range(n - 1)]
solve(n, A)

    