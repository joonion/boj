import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))
S.sort()
S = S[:(N-1)//2+1]
cnt = 0
while True:
    cnt += 1
    m = max(S) // 2
    if m == 0: break
    S.remove(m)
