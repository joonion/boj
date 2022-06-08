import sys
input = sys.stdin.readline

imv = [-1, 0, 1, 0]
jmv = [0, 1, 0, -1]

def move(d, i, j, n, m, A):
    global depth, path
    if 0 <= i < n and 0 <= j < m and path[ord(A[i][j]) - ord('A')] == 0:
        depth = max(depth, d)
        for x in range(4):
            path[ord(A[i][j])-ord('A')] = 1
            move(d + 1, i + imv[x], j + jmv[x], n, m, A)
            path[ord(A[i][j])-ord('A')] = 0

n, m = map(int, input().split())
A = [input().strip() for _ in range(n)]
path = [0] * 26
depth = 0
move(1, 0, 0, n, m, A)
print(depth)