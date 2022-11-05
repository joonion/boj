def is_palindrome(n):
    return str(n) == str(n)[::-1]

while True:
    n = int(input())
    if n == 0: break
    print('yes' if is_palindrome(n) else 'no')