def solve(n):
    return "yes" if str(n) == str(n)[::-1] else "no"
    
while True:
    n = int(input())
    if n == 0:
        break
    answer = solve(n)
    print(answer)