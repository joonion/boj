n = int(input())
m = input()[::-1]
A = []
for i in range(len(m)):
    A.append(n * int(m[i]) * 10 ** i)
for i in range(len(A)):
    print(A[i] // (10 ** i))
print(sum(A))