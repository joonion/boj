import sys
input = sys.stdin.readline

def solve(n, k, A):
    c = 0
    for i in range(1, n + 1):
        c += k // A[n - i]
        k %= A[n - i]
    print(c)

n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]
solve(n, k, A)