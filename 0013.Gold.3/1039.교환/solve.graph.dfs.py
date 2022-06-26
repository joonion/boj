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

def dfs(k, u, g):
    if k == 0:
        return u
    else:
        opt = -1
        for v in g[u]:
            opt = max(opt, dfs(k - 1, v, g))
        return opt

n, k = map(int, input().split())
g = {}
build_graph(n, g)
print(dfs(k, n, g))
