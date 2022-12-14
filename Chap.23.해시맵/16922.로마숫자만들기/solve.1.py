from itertools import combinations_with_replacement

def solve(n, t):
    s = set([])
    for c in combinations_with_replacement(t.keys(), n):
        s.add(sum([t[x] for x in c]))
    return len(s)

T = {'I':1, 'V':5, 'X':10, 'L':50}
N = int(input())
print(solve(N, T))