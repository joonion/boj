def solve(n, T):
    p = [0] * (n + 1)
    q = [1]
    while len(q) > 0:
        v = q.pop(0)
        for u in T[v]:
            if p[u] == 0:
                p[u] = v
                q.append(u)
    print("\n".join(map(str, p[2:])))
    
import sys
input = sys.stdin.readline
n = int(input())
T = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    T[u].append(v)
    T[v].append(u)
solve(n, T)