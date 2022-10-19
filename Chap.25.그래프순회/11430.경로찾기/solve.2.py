def bfs(v, A):
    queue = []
    visited = ["0"] * len(A)
    queue.append(v)
    while len(queue) > 0:
        v = queue.pop(0)
        for u in range(len(A)):
            if A[v][u] == "1" and visited[u] == "0":
                queue.append(u)
                visited[u] = "1"
    return visited

import sys
input = sys.stdin.readline

N = int(input())
A = [input().strip().split() for _ in range(N)]

B = []
for i in range(N):
    B.append(bfs(i, A))
for i in range(N):
    print(" ".join(B[i]))
