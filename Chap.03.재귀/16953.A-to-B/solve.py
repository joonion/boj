INF = 10 ** 9

def solve(a, b):
    if a == b:
        return 1
    elif a > b:
        return INF
    else:
        return 1 + min(solve(a * 2, b), solve(a * 10 + 1, b))
    
a, b = map(int, input().split())
answer = solve(a, b)
print(-1 if answer >= INF else answer)