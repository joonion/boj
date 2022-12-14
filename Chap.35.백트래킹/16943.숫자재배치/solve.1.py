from itertools import permutations

def solve(a, b):
    largest = -1
    for p in set(permutations(a)):
        x = int("".join(p))
        if p[0] != '0' and x < b:
            largest = max(largest, x)
    return largest

A, B = input().split()
print(solve(A, int(B)))
