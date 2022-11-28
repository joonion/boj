import sys
input = sys.stdin.readline
N = int(input())
S = [int(input()) for _ in range(N)]
T = {i:0 for i in S}
for n in S: T[n] += 1
print(sorted(list(T.items()), key = lambda x: (-x[1], x[0]))[0][0])