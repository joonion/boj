import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = set([input().strip() for _ in range(N)])
B = [input().strip() for _ in range(M)]
C = [1 for i in range(M) if B[i] in A]
print(len(C))
