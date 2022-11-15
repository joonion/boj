import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

def to_arabic(roman):
    n = 0
    for i in range(len(roman)):
        if i < len(roman) - 1 and T[roman[i]] < T[roman[i+1]]:
            n -= T[roman[i]]
        else:
            n += T[roman[i]]
    return n

def search(i, s, include):
    if i == len(s):
        return to_arabic(include)
    else:
        include.append(s[i])
        u = search(i + 1, s, include)
        include.pop()
        v = search(i + 1, s, include)
        return max(u, v)

def largest(s):
    return search(0, s, [])

def solve(str):
    s = [str[i] for i in range(len(str)) if str[i] in T]
    print(s)
    return 0 if len(s) == 0 else largest(s)

for _ in range(int(input())):
    print(solve(list(input().strip().upper())))
