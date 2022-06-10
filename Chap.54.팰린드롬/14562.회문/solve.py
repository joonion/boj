def palindrome(A, n):
    B = []
    while A > 0:
        B.append(A % n)
        A //= n
    return B == B[::-1]
    
T = int(input())
for _ in range(T):
    A, n = map(int, input().split())
    print(1 if palindrome(A, n) else 0)