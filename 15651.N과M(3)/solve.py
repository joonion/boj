from itertools import product

def solve(n, m):
    prods = product([i for i in range(1, n + 1)], repeat = m)
    for prod in prods:
        print(" ".join(map(str, list(prod))))

N, M = map(int, input().split())
solve(N, M)
