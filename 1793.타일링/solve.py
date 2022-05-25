def solve(n):
    if n <= 1:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, 2*a + b
        return b
    
while True:
    try:
        print(solve(int(input())))
    except:
        break
