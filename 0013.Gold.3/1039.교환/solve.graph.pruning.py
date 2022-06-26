def build_graph(n, g):
    s = list(map(int, str(n)))
    g[n] = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            s[i], s[j] = s[j], s[i]
            if s[0] != 0: g[n].add(int("".join(map(str, s))))
            s[i], s[j] = s[j], s[i]
    for x in g[n]:
        if x not in g:
            build_graph(x, g)

def bfs(k, u, g):
    visiting = {u}
    for _ in range(k):
        neighbors = set()
        for u in visiting:
            for v in g[u]:
                neighbors.add(v)
        if len(neighbors) == 0: return -1
        visiting = neighbors
    return max(visiting)

n, k = map(int, input().split())
g = {}
build_graph(n, g)
print(bfs(k, n, g))
