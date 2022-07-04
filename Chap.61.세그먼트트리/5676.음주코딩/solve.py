import sys
input = sys.stdin.readline
print = sys.stdout.write

def build(v, l, r, A, T):
    if l == r:
        T[v] = A[l]
    else:
        m = (l + r) // 2
        build(2*v, l, m, A, T)
        build(2*v+1, m+1, r, A, T)
        T[v] = T[2*v] * T[2*v+1]

def update(v, l, r, pos, val, T):
    if l == r:
        T[v] = val
    else:
        m = (l + r) // 2
        if pos <= m:
            update(2*v, l, m, pos, val, T)
        else:
            update(2*v+1, m+1, r, pos, val, T)
        T[v] = T[2*v] * T[2*v+1]

def query(v, l, r, L, R, T):
    if L > R:
        return 1
    elif l == L and r == R:
        return T[v]
    else:
        m = (l + r) // 2
        return query(2*v, l, m, L, min(R, m), T) * \
               query(2*v+1, m+1, r, max(L, m+1), R, T)

while True:
    try:
        n, m = map(int, input().split())
        A = [0] + list(map(int, input().split()))
        for i in range(len(A)):
            A[i] = 1 if A[i] > 0 else -1 if A[i] < 0 else 0
        T = [0] + [0] * (4 * n)
        build(1, 1, n, A, T)
        s = ""
        for _ in range(m):
            c, a, b = input().split()
            if c == 'C':
                update(1, 1, n, int(a), int(b), T)
            else:
                r = query(1, 1, n, int(a), int(b), T)
                s += "0" if r == 0 else "+" if r > 0 else "-"
        print(s + "\n")
    except:
        break
