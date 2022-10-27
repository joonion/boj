def isprime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

def check(d, n, m):
    if d == 1:
        for j in [2, 3, 5, 7]:
            if n <= j <= m: print(j)
    else:
        h = d // 2
        for i in range(10**(h-1), 10**h):
            s = str(i); r = s[::-1]
            r = "0" * (h - len(r)) + r
            if d % 2 == 0:
                p = int(f"{s}{r}")
                if n <= p <= m and isprime(p): print(p)
            else:
                for j in range(10):
                    p = int(f"{s}{j}{r}")
                    if n <= p <= m and isprime(p): print(p)
    
def solve(n, m):
    d1, d2 = len(str(n)), len(str(m))
    for d in range(d1, d2 + 1):
        check(d, n, m)
    print('-1')
    
n, m = map(int, input().split())
solve(n, m)
