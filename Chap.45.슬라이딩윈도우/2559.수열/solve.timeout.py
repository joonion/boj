def solve(n, k, A):
    opt = -100 * n
    for i in range(n - k):
        opt = max(opt, sum(A[i:i+k]))
    return opt

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
A = list(map(int, input().split()))
print(solve(n, k, A))