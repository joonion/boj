import sys
input = sys.stdin.readline
N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]
TX = {p[0]:0 for p in P}
TY = {p[1]:0 for p in P}
for x, y in P:
    TX[x] += 1
    TY[y] += 1
cnt = 0
for t in list(TX.values()) + list(TY.values()):
    cnt += t > 1
print(cnt)
    
    
