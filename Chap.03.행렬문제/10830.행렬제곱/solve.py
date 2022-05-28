def mmult(n, A, B):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    for i in range(n):
        for j in range(n):
                C[i][j] = C[i][j] % 1000
    return C

def mpower(A, n, m):
    if m == 1:
        for i in range(n):
            for j in range(n):
                    A[i][j] = A[i][j] % 1000
        return A
    elif m % 2 == 1:
        C = mpower(A, n, m - 1)
        return mmult(n, A, C)
    else:
        C = mpower(A, n, m // 2)
        return mmult(n, C, C)

def solve(A, n, m):
    C = mpower(A, n, m)
    for i in range(len(C)):
        for j in range(len(C)):
            print(C[i][j], end = " ")
        print()
        
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
solve(A, N, B)
