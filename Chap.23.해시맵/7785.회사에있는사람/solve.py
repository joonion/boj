import sys
input = sys.stdin.readline

n = int(input())
log = [input().strip().split() for _ in range(n)]
T = {log[i][0]:0 for i in range(n)}
for i in range(n):
    T[log[i][0]] = 1 if log[i][1] == "enter" else 0
p = [item[0] for item in T.items() if item[1] == 1]
p.sort(reverse = True)
print("\n".join(p))
