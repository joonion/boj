def lcm(n, m):
    return (n * m) // gcd(n, m)

def gcd(n, m):
    if m == 0:
        return n 
    else:
        return gcd(m, n % m)
    
def solve(n, m):
    return gcd(n, m), lcm(n, m)

N, M = map(int, input().split())
answer1, answer2 = solve(N, M)
print(answer1)
print(answer2)
