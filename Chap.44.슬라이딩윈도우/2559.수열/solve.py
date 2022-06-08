def solve(n, k, A):
    opt = S = sum(A[:k])
    for i in range(n - k):
        S = S - A[i] + A[i + k]
        opt = max(opt, S)
    return opt

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
A = list(map(int, input().split()))
print(solve(n, k, A))