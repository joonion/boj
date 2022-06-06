import sys
input = sys.stdin.readline
n = int(input())
A = []
for i in range(n):
    age, name = input().strip().split()
    A.append((int(age), i, name))
A.sort()
for i in range(n):
    print(A[i][0], A[i][2])