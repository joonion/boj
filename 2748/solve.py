def solve(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
    
N = int(input())
answer = solve(N)
print(answer)