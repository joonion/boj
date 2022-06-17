n = int(input())
A = map(int, input().split())

from itertools import permutations
perm = permutations(A, n)
largest = 0
for p in perm:
    B = list(p)
    s = 0
    for i in range(n - 1):
        s += abs(B[i] - B[i+1])
    largest = max(largest, s)
print(largest)        