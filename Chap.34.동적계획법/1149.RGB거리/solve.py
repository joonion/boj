import sys
input = sys.stdin.readline

def solve(n, A):
    for i in range(1, n):
        A[i][0] += min(A[i - 1][1], A[i - 1][2])
        A[i][1] += min(A[i - 1][0], A[i - 1][2])
        A[i][2] += min(A[i - 1][0], A[i - 1][1])
    return min(A[n - 1])    

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, A))