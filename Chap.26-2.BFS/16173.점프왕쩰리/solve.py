def bfs(n, A):
    di, dj = [0, 1], [1, 0]
    queue = []
    queue.append((0, 0))
    visited = [[0] * n for _ in range(n)]
    while queue:
        i, j = queue.pop(0)
        if A[i][j] == -1: return True
        for k in range(2):
            ni, nj = i + di[k]*A[i][j], j + dj[k]*A[i][j]
            if ni < n and nj < n and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = True
    return False

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
print("HaruHaru" if bfs(N, A) else "Hing")
