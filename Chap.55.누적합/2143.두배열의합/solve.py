from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

def cumsum(A):
    X = []
    for i in range(1, len(A)):
        A[i] += A[i - 1]
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            X.append(A[j] - A[i])
    return X

def solve(A, B, T):
    X, Y = sorted(cumsum(A)), sorted(cumsum(B))
    cnt = 0
    for i in range(len(X)):
        left = bisect_left(Y, T - X[i])
        right = bisect_right(Y, T - X[i])
        cnt += right - left
    return cnt
    
T = int(input())
n = int(input())
A = [0] + list(map(int, input().split()))
m = int(input())
B = [0] + list(map(int, input().split()))
print(solve(A, B, T))

