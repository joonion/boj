from heapq import heappush, heappop
import sys
input = sys.stdin.readline

INF = 10 ** 8 - 1

def dijkstra(s, G):
    dist, PQ = [INF] * len(G), []
    dist[s] = 0
    heappush(PQ, (0, s))
    while len(PQ) > 0:
        u = heappop(PQ)[1]
        for v in G[u].keys():
            if dist[u] + G[u][v] < dist[v]:
                dist[v] = dist[u] + G[u][v]
                heappush(PQ, (dist[v], v))
    return dist

n, m = map(int, input().split())
s = int(input())
G = {v:{} for v in range(n + 1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    G[u][v] = w if v not in G[u] else min(G[u][v], w)
dist = dijkstra(s, G)
for i in range(1, n + 1):
    print("INF" if dist[i] == INF else dist[i])