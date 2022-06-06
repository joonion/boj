import sys
input = sys.stdin.readline

def solve(n):
    sqrtn = int(n**0.5)
    if sqrtn ** 2 == n:
        return 1
    s1 = {i**2 for i in range(1, sqrtn + 1)}
    s2 = {i + j for i in s1 for j in s1}
    if n in s2:
        return 2
    for i in s1:
        if n - i in s2:
            return 3
    return 4

print(solve(int(input())))