import sys
input = sys.stdin.readline
print = sys.stdout.write

def isprime(n):
    if n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
    return True if n > 1 else False

def solve(n, m):
    for k in range(n, m + 1):
        s = str(k)
        if s == s[::-1] and isprime(k):
            print(s)
            print("\n")
    print('-1')
    
n, m = map(int, input().split())
solve(n, m)
