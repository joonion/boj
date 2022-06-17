n = int(input())
A = list(map(int, input().split()))
A.sort()
for i in range(1, len(A)):
    A[i] += A[i-1]
print(sum(A))
    