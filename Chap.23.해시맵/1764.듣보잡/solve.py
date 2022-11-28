import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = set([input().strip() for _ in range(N)])
B = set([input().strip() for _ in range(M)])
C = A & B
D = sorted(list(C))
print(len(D))
print("\n".join(D))
