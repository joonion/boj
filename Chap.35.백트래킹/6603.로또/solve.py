from itertools import combinations

def solve(k, s):
    for c in combinations(s, 6):
        print(" ".join(map(str, c)))

while True:
    k, *s = map(int, input().split())
    if k == 0: break
    solve(k, s)
    print()