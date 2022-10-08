from math import floor, sqrt

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, floor(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve(n):
    while True:
        if is_prime(n) and is_palindrome(n):
            return n
        n += 1
        
N = int(input())
print(solve(N))
