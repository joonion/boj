def solve(n):
    if n <= 2:
        return n
    else:
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, (a + b) % 10007
        return b

n = int(input())    
answer = solve(n)
print(answer)