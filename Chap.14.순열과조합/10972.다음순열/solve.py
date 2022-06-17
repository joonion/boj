n = int(input())
A = list(map(int, input().split()))
if A[::-1] == sorted(A):
    print(-1)
else:
    s = A[-1]
    for i in range(n, -1, -1):
        if s < A[i]:
    