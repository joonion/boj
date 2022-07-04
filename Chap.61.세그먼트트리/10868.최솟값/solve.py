import sys
input = sys.stdin.readline

def build(v, l, r, A, T):
    if l == r:
        T[v] = A[l]
    else:
        m = (l + r) // 2
        build(2*v, l, m, A, T)
        build(2*v+1, m+1, r, A, T)
        T[v] = min(T[2*v], T[2*v+1])

def search(v, l, r, L, R, T):
    if L > R:
        return 10 ** 9
    elif l == L and r == R:
        return T[v]
    else:
        m = (l + r) // 2
        return min(search(2*v, l, m, L, min(R, m), T), \
                   search(2*v+1, m+1, r, max(L, m+1), R,         T))

n, m = map(int, input().split())
A = [0] + [int(input()) for _ in range(n)]
T = [0] + [0] * (4 * n)
build(1, 1, n, A, T)
for _ in range(m):
    a, b = map(int, input().split())
    smallest = search(1, 1, n, a, b, T)
    print(smallest)