def solve(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
n = int(input())
print(solve(n))