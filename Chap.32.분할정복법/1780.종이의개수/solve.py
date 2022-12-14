import sys
input = sys.stdin.readline

def check(i, j, n, A):
    chk = A[i][j]
    for r in range(i, i + n):
        for c in range(j, j + n):
            if chk != A[r][c]: return 2
    return chk

def solve(i, j, n, A, T):
    chk = check(i, j, n, A)
    if chk in [-1, 0, 1]:
        T[chk] += 1
    else:
        m = n // 3
        for r in range(i, i + n, m):
            for c in range(j, j + n, m):
                solve(r, c, m, A, T)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
T = {-1:0, 0:0, 1:0}
solve(0, 0, N, A, T)
print(T[-1])
print(T[0])
print(T[1])
