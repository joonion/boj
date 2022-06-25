def bfs(n, k):
    queue = [n]
    dist = [-1] * 100001
    dist[n] = 0
    while queue and dist[k] < 0:
        x = queue.pop(0)
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 100000 and dist[nx] < 0:
                queue.append(nx)
                dist[nx] = dist[x] + 1
    return dist[k]

n, k = map(int, input().split())
print(bfs(n, k))