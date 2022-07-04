def solve(k, n):
    A = [[0] * n for _ in range(k + 1)]
    for i in range(1, n + 1):
        A[0][i-1] = i
    for i in range(1, k + 1):
        for j in range(n):
            A[i][j] = sum(A[i-1][:j+1])
    return A[k][n - 1]

for _ in range(int(input())):
    k, n = int(input()), int(input())
    print(solve(k, n))