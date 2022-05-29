imove = [0, 1, 0, -1]
jmove = [1, 0, -1, 0]

mindepth = 1000000000

def adjacent(u, n, m, maze, mark):
    global imove, jmove
    i, j = u // m, u % m
    neighbors = []
    for d in range(4):
        ni, nj = i + imove[d], j + jmove[d]
        if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] == 1 and not mark[ni * m + nj]:
            neighbors.append(ni * m + nj)
    return neighbors
            
def solve(n, m, maze):
    global mindepth
    queue = []
    mark = [False] * (n * m)
    queue.append((0, 1))
    mark[0] = True
    while len(queue) > 0:
        (v, depth) = queue.pop(0)
        if v == n * m - 1:
            mindepth = min(mindepth, depth)
        for u in adjacent(v, n, m, maze, mark):
            queue.append((u, depth + 1))
            mark[u] = True
    return mindepth
    
N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
answer = solve(N, M, maze)
print(answer)