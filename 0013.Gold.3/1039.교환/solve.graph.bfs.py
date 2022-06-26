def build_graph(n, g):
    s = list(map(int, str(n)))
    g[n] = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            s[i], s[j] = s[j], s[i]
            m = int("".join(map(str, s)))
            if s[0] != 0 and m not in g[n]:
                g[n].append(m)
            s[i], s[j] = s[j], s[i]
    for x in g[n]:
        if x not in g:
            build_graph(x, g)

def bfs(k, u, g):
    queue = [(u, 0)]
    largest = -1
    while queue:
        u, d = queue.pop(0)
        if d == k:
            largest = max(largest, u)
        else:
            for v in g[u]:
                queue.append((v, d + 1))
    return largest

n, k = map(int, input().split())
g = {}
build_graph(n, g)
print(bfs(k, n, g))
