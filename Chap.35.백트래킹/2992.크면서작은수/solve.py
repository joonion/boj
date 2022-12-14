from itertools import permutations

def solve(s):
    v, minv = int(s), 10**9
    for p in permutations(s):
        t = int("".join(p))
        if t > v:
            minv = min(minv, t)
    return minv if minv < 10**9 else 0

s = input()
print(solve(s))
