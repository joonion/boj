import sys
input = sys.stdin.readline

INF = 10 ** 10

def subsets_containing_k_vertices(n, k):
    S = []
    for A in range(2 ** (n-1)):
        if bin(A).count("1") == k:
            S.append(A)
    return S

def not_in_A(n, A):
    S = []
    for i in range(n - 1):
        if A & (1 << i) == 0:
            S.append(2 + i)
    return S

def in_A(n, A):
    S = []
    for i in range(n - 1):
        if A & (1 << i) != 0:
            S.append(2 + i)
    return S

def diff(A, j):
    return A & ~(1 << (j - 2))

def minimum(n, i, A, W, D):
    minvalue = INF
    for j in in_A(n, A):
        minvalue = min(minvalue, W[i][j] + D[j][diff(A, j)])
    return minvalue

def solve(n, W):
    D = [[INF] * (2**(n-1)) for _ in range(n + 1)]
    for i in range(2, n + 1):
        D[i][0] = W[i][1]
    for k in range(1, n - 1):
        for A in subsets_containing_k_vertices(n, k):
            for i in not_in_A(n, A):
                D[i][A] = minimum(n, i, A, W, D)
    A = 2 ** (n - 1) - 1 # A = V - {v1}
    D[1][A] = minimum(n, 1, A, W, D)
    return D[1][A]
        
n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if W[i][j] == 0:
            W[i][j] = INF
for i in range(n):
    W[i][i] = 0
for i in range(n):
    W[i] = [0] + W[i]
W.insert(0, [0] * (n + 1))
print(solve(n, W))