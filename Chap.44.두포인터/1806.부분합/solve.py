import sys
input = sys.stdin.readline

def solve(n, S, A):
    for i in range(1, n):
        A[i] += A[i - 1]
    A = [0] + A
    opt = 2 ** 32
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if A[j] - A[i] > S:
                opt = min(opt, j - i)
                break
    return opt

n, S = map(int, input().split())
A = list(map(int, input().split()))
print(solve(n, S, A))