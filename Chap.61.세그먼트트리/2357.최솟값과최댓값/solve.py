import sys
input = sys.stdin.readline

def build(v, l, r, A, T):
    if l == r:
        T[v] = (A[l], A[l])
    else:
        m = (l + r) // 2
        build(2*v, l, m, A, T)
        build(2*v+1, m+1, r, A, T)
        T[v] = (min(T[2*v][0], T[2*v+1][0]), \
                max(T[2*v][1], T[2*v+1][1]))

def search(v, l, r, L, R, T):
    if L > R:
        return (10 ** 9, 0)
    elif l == L and r == R:
        return T[v]
    else:
        m = (l + r) // 2
        a, b = search(2*v, l, m, L, min(R, m), T)
        c, d = search(2*v+1, m+1, r, max(L, m+1), R, T)
        return (min(a, c), max(b, d))

n, m = map(int, input().split())
A = [0] + [int(input()) for _ in range(n)]
T = [0] + [0] * (4 * n)
build(1, 1, n, A, T)
for _ in range(m):
    a, b = map(int, input().split())
    s, l = search(1, 1, n, a, b, T)
    print(s, l)
