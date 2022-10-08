def build(d, P, T):
    if len(P) == 1:
        T[d].append(P[0])
    else:
        m = len(P) // 2
        T[d].append(P[m])
        build(d + 1, P[:m], T)
        build(d + 1, P[m+1:], T)

def solve(k, P):
    T = [[] for _ in range(k)]
    build(0, P, T)
    return T

k = int(input())
P = list(map(int, input().split()))
T = solve(k, P)
for i in range(k):
    print(" ".join(map(str, T[i])))
