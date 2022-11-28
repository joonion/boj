def solve(G):
    pass

for _ in range(int(input())):
    N, M = map(int, input().split())
    G = {i:[] for i in range(1, N + 1)}
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    # print(solve(G))
    print(G)
    