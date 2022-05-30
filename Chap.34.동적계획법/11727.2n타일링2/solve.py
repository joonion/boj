def solve(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 3
    else:
        a, b = 1, 3
        for _ in range(3, n + 1):
            a, b = b, (2 * a + b) % 10007
        return b 

n = int(input())    
answer = solve(n)
print(answer)