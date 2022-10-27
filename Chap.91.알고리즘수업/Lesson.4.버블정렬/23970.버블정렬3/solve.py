import sys
input = sys.stdin.readline

def solve(n, A, B):
    cnt = 0
    for last in range(n, 1, -1):
        for i in range(1, last):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                cnt += 1
                if A == B:
                    print(1)
                    return
    print(0)

N = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
solve(N, A, B)