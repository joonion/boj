import sys
input = sys.stdin.readline

def update(v, l, r, pos, val, T):
    if l == r:
        T[v] += val
    else:
        m = (l + r) // 2
        if pos <= m:
            update(2*v, l, m, pos, val, T)
        else:
            update(2*v+1, m+1, r, pos, val, T)
        T[v] = T[2*v] + T[2*v+1]

def query(v, l, r, k, T):
    if l == r:
        return l
    else:
        m = (l + r) // 2
        if k <= T[2*v]:
            return query(2*v, l, m, k, T)
        else:
            return query(2*v+1, m+1, r, k-T[2*v], T)

n, k = map(int, input().split())
A = [int(input()) for _ in range(n)]
MAX = 65536
T = [0] * (4*MAX+1)
q, s = [], 0
for a in A:
    q.append(a)
    update(1, 1, MAX, a + 1, 1, T)
    if len(q) == k:
        s += query(1, 1, MAX, (k + 1) // 2, T) - 1
        b = q.pop(0)
        update(1, 1, MAX, b + 1, -1, T)
print(s)