INF = 10 ** 8 - 1

def nearest(n, dist, mark, G):
    vnear, minlength = -1, INF
    for v in range(1, n + 1):
        if not mark[v] and dist[v] < minlength:
            vnear, minlength = v, dist[v]
    return vnear
        
def dijkstra(n, s, G):
    dist, mark = [INF] * len(G), [0] * len(G)
    dist[s], mark[s] = 0, 1
    for u in G[s].keys():
        dist[u] = G[s][u]
    for _ in range(n - 1):
        u = nearest(n, dist, mark, G)
        if u < 0: break
        for v in range(1, n + 1):
            if v in G[u] and dist[u] + G[u][v] < dist[v]:
                dist[v] = dist[u] + G[u][v]
        mark[u] = 1
    return dist

n, m = map(int, input().split())
s = int(input())
G = {v:{} for v in range(n + 1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    G[u][v] = w if v not in G[u] else min(G[u][v], w)
dist = dijkstra(n, s, G)
for i in range(1, n + 1):
    print("INF" if dist[i] == INF else dist[i])