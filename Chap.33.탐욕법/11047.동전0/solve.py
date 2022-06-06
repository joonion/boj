import sys
input = sys.stdin.readline

def solve(k, A):
    t, count = len(A) - 1, 0
    while k > 0:
        count += k // A[t]
        k %= A[t]
        t -= 1
    return count

n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]
answer = solve(k, A)
print(answer)
