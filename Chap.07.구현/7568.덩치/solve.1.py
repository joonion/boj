def solve(n, A):
    D = [1] * n
    for i in range(n):
        for j in range(n):
            if A[i][0] < A[j][0] and A[i][1] < A[j][1]:
                D[i] += 1
    for i in range(n):
        print(D[i], end = " ")

N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)] 
solve(N, A)
