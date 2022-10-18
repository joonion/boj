def mult(n, m, A, B):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            t = 0
            for k in range(n):
                t += A[i][k] * B[k][j]
            C[i][j] = t % m
    return C

def mpower(n, m, p, A):
    if p == 1:
        return A
    elif p % 2 == 0:
        B = mpower(n, m, p // 2, A)
        return mult(n, m, B, B)
    else:
        B = mpower(n, m, p // 2, A)
        return mult(n, m, A, mult(n, m, B, B))

import sys
input = sys.stdin.readline

while True:
    n, m, p = map(int, input().split())
    if n == 0: break
    A = [list(map(int, input().split())) for _ in range(n)]
    B = mpower(n, m, p, A)
    for i in range(n):
        for j in range(n):
            print(B[i][j], end = " ")
        print()
    print()
