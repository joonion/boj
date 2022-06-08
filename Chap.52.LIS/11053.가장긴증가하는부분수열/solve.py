def solve(n, A):
    D = [1] * n
    for i in range(n):
        for j in range(i):
            if A[i] > A[j] and D[i] < D[j] + 1:
                D[i] = D[j] + 1
    return max(D)

n = int(input())
A = list(map(int, input().split()))
print(solve(n, A))