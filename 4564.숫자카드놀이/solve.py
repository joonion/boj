def solve(n):
    print(n, end = " ")
    s = str(n)
    if len(s) > 1:
        prod = 1
        for i in range(len(s)):
            prod *= int(s[i])
        solve(prod)
    
while True:
    S = int(input())
    if S == 0:
        break
    solve(S)
    print()
