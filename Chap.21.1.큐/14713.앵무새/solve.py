def valid(x, n, s):
    for i in range(n):
        if len(s[i]) > 0 and x == s[i][0]:
            s[i].pop(0)
            return True
    return False
        
def solve(n, s, t):
    for x in t:
        if not valid(x, n, s):
            return False
    return sum([len(i) for i in s]) == 0

N = int(input())
S = []
for _ in range(N):
    S.append(input().split())
T = input().split()
print("Possible" if solve(N, S, T) else "Impossible")
