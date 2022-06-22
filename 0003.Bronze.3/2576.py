A = [int(input()) for _ in range(7)]
s = 100
S = 0
for a in A:
    if a % 2 == 1:
        S += a 
        s = min(s, a)
if s == 100: print(-1)
else: print(S); print(s)
    