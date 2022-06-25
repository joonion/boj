def prod(s):
    p = 1
    for c in s:
        p *= int(c)
    return p

def solve(n):
    s = str(n)
    for p in range(1, len(s)):
        if prod(s[:p]) == prod(s[p:]):
            return True
    return False
        
n = int(input())
print("YES" if solve(n) else "NO")