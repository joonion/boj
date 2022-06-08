def minimum(n, A):
    if n == 1:
        return min(A[0])
    else:
        D = [[0] * 3, [0] * 3]
        for i in range(n - 1, -1, -1):
            cur, nxt = i % 2, (i - 1) % 2
            D[nxt][0] = A[i][0] + min(D[cur][0], D[cur][1])
            D[nxt][1] = A[i][1] + min(D[cur])
            D[nxt][2] = A[i][2] + min(D[cur][1], D[cur][2])
        return min(D[1])

def maximum(n, A):
    if n == 1:
        return max(A[0])
    else:
        D = [[0] * 3, [0] * 3]
        for i in range(n - 1, -1, -1):
            cur, nxt = i % 2, (i - 1) % 2
            D[nxt][0] = A[i][0] + max(D[cur][0], D[cur][1])
            D[nxt][1] = A[i][1] + max(D[cur])
            D[nxt][2] = A[i][2] + max(D[cur][1], D[cur][2])
        return max(D[1])

import sys
input = sys.stdin.readline
n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
print(maximum(n, A), minimum(n, A))
