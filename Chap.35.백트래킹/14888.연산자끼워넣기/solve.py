from itertools import permutations

def solve(n, p, q):
    op = [0]*q[0] + [1]*q[1] + [2]*q[2] + [3]*q[3]
    minv, maxv = 10**9, -10**9
    for t in permutations(op):
        v = p[0]
        for i in range(n - 1):
            if t[i] == 0: v += p[i+1]
            elif t[i] == 1: v -= p[i+1]
            elif t[i] == 2: v *= p[i+1]
            elif t[i] == 3:
                if v >= 0: v //= p[i+1]
                else: v = -((-v) // p[i+1])
        minv = min(minv, v)    
        maxv = max(maxv, v)
    print(maxv)
    print(minv)
    
n, *a = map(int, open(0).read().split())
solve(n, a[:n], a[n:])
