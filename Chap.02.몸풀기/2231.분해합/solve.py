def sumdigits(n):
    m, s = n, 0
    while m > 0:
        s += m % 10
        m = m // 10
    return n + s
        
def solve(N):
    for i in range(1, N + 1):
        if sumdigits(i) == N:
            return i
    return 0
    
N = int(input())
answer = solve(N)
print(answer)