import sys
input = sys.stdin.readline

def update(v, l, r, pos, T):
    if l == r:
        T[v] += 1
    else:
        m = (l + r) // 2
        if pos <= m:
            update(2*v, l, m, pos, T)
        else:
            update(2*v+1, m+1, r, pos, T)
        T[v] = T[2*v] + T[2*v+1]

def query(v, l, r, L, R, T):
    if r < L or R < l:
        return 0
    elif L <= l and r <= R:
        return T[v]
    else:
        m = (l + r) // 2
        return query(2*v, l, m, L, R, T) + \
               query(2*v+1, m+1, r, L, R, T)

def solve(n, A):
    A.sort(key = lambda x: x[1])
    j, t = 0, -(10**9+1)
    for i in range(n):
        if A[i][1] > t: j += 1; t = A[i][1]
        A[i][1] = j
    A.sort(key = lambda x: (x[0], -x[1]))
    T = [0] * (4*n+1)
    S = 0
    for a in A:
        S += query(1, 1, n, a[1], n, T)
        update(1, 1, n, a[1], T)
    print(S)
        
for _ in range(int(input())):
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]
    solve(n, A)
