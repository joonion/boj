def solve(n, A, B):
    A.sort()
    B.sort(reverse = True)
    S = 0
    for i in range(n):
        S += A[i] * B[i]
    return S

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solve(n, A, B))
