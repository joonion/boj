def bfs(v, A):
    queue = []
    visited = [0] * len(A)
    queue.append(v)
    while len(queue) > 0:
        v = queue.pop(0)
        for u in range(len(A)):
            if A[v][u] == 1 and visited[u] == 0:
                queue.append(u)
                visited[u] = 1
    return visited

def solve(n, A):
    B = []
    for i in range(n):
        B.append(bfs(i, A))
    for i in range(n):
        print(" ".join(map(str, B[i])))
            
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
solve(N, A)
