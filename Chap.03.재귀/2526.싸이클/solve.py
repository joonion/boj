def iterative(n, p):
    m, s = n, [n]
    while True:
        m = (m*n) % P
        if m in s: break
        s.append(m)
    return len(s) - s.index(m)

def recursive(n, p, m, s):
    m = (m*n) % p
    if m in s:
        return len(s) - s.index(m)
    else:
        return recursive(n, p, m, s + [m])
    
def solve(N, P):
    return recursive(N, P, N, [N])
    # return iterative(N, P)
    
N, P = map(int, input().split())
print(solve(N, P))