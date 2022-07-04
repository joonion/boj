import sys
input = sys.stdin.readline

def build(v, l, r, A, T):
    if l == r:
        T[v] = A[l]
    else:
        m = (l + r) // 2
        build(2 * v, l, m, A, T)
        build(2 * v + 1, m + 1, r, A, T)
        T[v] = T[2 * v] + T[2 * v + 1]

def update(v, l, r, pos, val, T):
    if l == r:
        T[v] = val
    else:
        m = (l + r) // 2
        if pos <= m:
            update(2 * v, l, m, pos, val, T)
        else:
            update(2 * v + 1, m + 1, r, pos, val, T)
        T[v] = T[2 * v] + T[2 * v + 1]
    
def sumofrange(v, l, r, L, R, T):
    if L > R:
        return 0
    elif l == L and r == R:
        return T[v]
    else:
        m = (l + r) // 2
        return sumofrange(2 * v, l, m, L, min(R, m), T) + \
               sumofrange(2 * v + 1, m + 1, r, max(L, m + 1), R, T)

n, m, k = map(int, input().split())
A = [0] + [int(input()) for _ in range(n)]
T = [0] + [0] * (4 * n)
build(1, 1, n, A, T)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(1, 1, n, b, c, T)
    elif a == 2:
        print(sumofrange(1, 1, n, b, c, T))