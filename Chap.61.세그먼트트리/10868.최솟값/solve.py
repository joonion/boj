import sys
input = sys.stdin.readline

def build(i, l, r, A, T):
    if l == r:
        T[i] = A[l]
    else:
        m = (l + r) // 2
        build(2*i, l, m, A, T)
        build(2*i+1, m+1, r, A, T)
        T[i] = min(T[2*i], T[2*i+1])

def query(i, l, r, L, R, T):
    if R < l or r < L:
        return 10 ** 9
    elif L <= l and r <= R:
        return T[i]
    else:
        m = (l + r) // 2
        return min(query(2*i,   l,   m, L, R, T), \
                   query(2*i+1, m+1, r, L, R, T))

n, m = map(int, input().split())
A = [0] + [int(input()) for _ in range(n)]
T = [0] + [0] * (4 * n)
build(1, 1, n, A, T)
for _ in range(m):
    a, b = map(int, input().split())
    print(query(1, 1, n, a, b, T))