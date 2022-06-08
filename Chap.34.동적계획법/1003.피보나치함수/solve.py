def solve(n):
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    else:
        zero0, zero1 = 1, 0
        one0, one1 = 0, 1
        for _ in range(2, n + 1):
            zero0, zero1 = zero1, zero0 + zero1
            one0, one1 = one1, one0 + one1
        return zero1, one1
    
T = int(input())
for _ in range(T):
    n = int(input())
    ans1, ans2 = solve(n)
    print(ans1, ans2)
    