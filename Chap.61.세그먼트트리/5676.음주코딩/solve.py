import sys
input = sys.stdin.readline

def build(i, l, r, A, T):
    if l == r:
        T[i] = 1 if A[l] > 0 else -1 if A[l] < 0 else 0
    else:
        m = (l + r) // 2
        build(2*i, l, m, A, T)
        build(2*i+1, m+1, r, A, T)
        T[i] = T[2*i] * T[2*i+1]

def update(i, l, r, pos, val, T):
    if l == r:
        T[i] = 1 if val > 0 else -1 if val < 0 else 0
    else:
        m = (l + r) // 2
        if pos <= m:
            update(2*i, l, m, pos, val, T)
        else:
            update(2*i+1, m+1, r, pos, val, T)
        T[i] = T[2*i] * T[2*i+1]

def query(i, l, r, L, R, T):
    if R < l or r < L:
        return 1
    elif L <= l and r <= R:
        return T[i]
    else:
        m = (l + r) // 2
        return query(2*i,   l,   m, L, R, T) * \
               query(2*i+1, m+1, r, L, R, T)

while True:
    try:
        n, m = map(int, input().split())
        A = [0] + list(map(int, input().split()))
        T = [0] + [0] * (4 * n)
        build(1, 1, n, A, T)
        s = ""
        for _ in range(m):
            c, a, b = input().split()
            if c == 'C':
                update(1, 1, n, int(a), int(b), T)
            else:
                r = query(1, 1, n, int(a), int(b), T)
                s += "+" if r > 0 else "-" if r < 0 else "0"
        print(s)
    except: break