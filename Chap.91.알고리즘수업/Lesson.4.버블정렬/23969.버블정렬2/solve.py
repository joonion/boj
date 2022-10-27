import sys
input = sys.stdin.readline

def solve(n, k, A):
    cnt = 0
    for last in range(n, 1, -1):
        for i in range(1, last):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                cnt += 1
                if cnt == k:
                    print(" ".join(map(str, A[1:])))
                    return
    print(-1)

N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
solve(N, K, A)