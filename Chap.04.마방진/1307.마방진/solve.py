def inc(i, n):
    return 0 if i == n - 1 else i + 1

def dec(i, n):
    return n - 1 if i == 0 else i - 1

def magic_odd(n, A):
    i, j = 0, n // 2
    for k in range(1, n * n + 1):
        A[i][j] = k
        ni, nj = dec(i, n), inc(j, n)
        i = inc(i, n) if A[ni][nj] != 0 else ni
        j = j if A[ni][nj] != 0 else nj
        
def magic_power_of_four(n, A):
    L = [[1 + i * n + j for j in range(n)] for i in range(n)]
    R = [[n * n - i * n - j for j in range(n)] for i in range(n)]
    for si in range(0, n, 4):
        for sj in range(0, n, 4):
            for i in range(4):
                for j in range(4):
                    if i == j or i + j == 3:
                        A[si + i][sj + j] = L[si + i][sj + j]
                    else:
                        A[si + i][sj + j] = R[si + i][sj + j]

def magic_four_plus_two(n, A):
    m = n // 2
    B = [[0] * m for _ in range(m)]
    magic_odd(m, B)
    for i in range(m):
        for j in range(m):
            A[i][j] = B[i][j]
            A[i + m][j + m] = B[i][j] + m * m
            A[i][j + m] = B[i][j] + 2 * m * m
            A[i + m][j] = B[i][j] + 3 * m * m
    k = (m - 1) // 2
    for i in range(m):
        for j in range(k):
            A[i][j], A[i + m][j] = A[i + m][j], A[i][j]
    for i in range(m):
        for j in range(n - 1, n - k, -1):
            A[i][j], A[i + m][j] = A[i + m][j], A[i][j]
    mid = m // 2
    for j in range(k - 1, k + 1):
        A[mid][j], A[m + mid][j] = A[m + mid][j], A[mid][j]
    
def solve(n):
    A = [[0] * N for _ in range(N)]
    if n % 2 == 1:
        magic_odd(n, A)
    elif n % 4 == 0:
        magic_power_of_four(n, A)
    else:
        magic_four_plus_two(n, A)
    for i in range(n):
        for j in range(n):
            print(A[i][j], end = " ")
        print()
    
N = int(input())
solve(N)
