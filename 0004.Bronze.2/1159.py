import sys
input = sys.stdin.readline

n = int(input())
A = [input()[0] for _ in range(n)]

from collections import Counter
B = Counter(A)
C = filter(lambda x: 4 < B[x], B)
D = "".join(sorted(C))
print("PREDAJA" if len(D) == 0 else D)