n, m = map(int, input().split())
A = [input() for _ in range(n)]
r = 0
for i in range(n):
    if A[i].count('X') == 0: r+= 1
c = 0
for h in [*zip(*A)]:
    if h.count('X') == 0: c+= 1
print(max(r, c))