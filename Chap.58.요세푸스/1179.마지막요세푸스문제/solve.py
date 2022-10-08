import sys
sys.setrecursionlimit(10**6)

def f(n, k):
    if n == 1: return 0
    if k == 1: return n - 1
    if 1 < n <= k:
        return (f(n - 1, k) + k) % n
    else:
        m = n // k
        t = (f(n - m, k) - n % k) % (n - m)
        return k * t // (k - 1)

n, k = map(int, input().split())
print(f(n, k) + 1)