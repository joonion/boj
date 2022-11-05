def is_palindrome(s):
    return s == s[::-1]
    
def solve(s):
    low, high = 0, len(s) - 1
    while low < high:
        if s[low] == s[high]:
            low += 1; 
            high -= 1
        elif is_palindrome(s[low+1:high+1]) or is_palindrome(s[low:high]):
            return 1
        else:
            return 2
    return 0

T = int(input())
for _ in range(T):
    S = input()
    print(solve(S))
    