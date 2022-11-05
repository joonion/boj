def base(n, b):
    s = []
    while n != 0:
        s.append(n % b)
        n //= b
    return s
        
def solve(n):
    check = True
    for i in range(2, 11):
        s = base(n, i)
        if s == s[::-1]:
            print(i, "".join(map(str, s)))
            check = False
    if check:
        print("NIE")
        
N = int(input())
solve(N)