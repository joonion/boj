def dfs(i, a, b, n, g, v):
    if a == b:
        return i
    else:
        minv = 1001
        for c in g[a]:
            if not v[c]:
                v[c] = True
                minv = min(minv, dfs(i + 1, c, b, n, g, v))
        return -1 if minv == 1001 else minv

def solve(a, b, n, g):
    visited = [False] * (n + 1)
    return dfs(0, a, b, n, g, visited)
    
n = int(input())
a, b = map(int, input().split())
g = {i:[] for i in range(1, n + 1)}
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)
print(solve(a, b, n, g))