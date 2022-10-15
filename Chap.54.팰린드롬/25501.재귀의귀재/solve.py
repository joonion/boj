def recursion(s, l, r, c):
    if l >= r:
        return 1, c + 1
    elif s[l] != s[r]:
        return 0, c + 1
    else:
        return recursion(s, l+1, r-1, c+1)
    
def isPalindrome(S):
    return recursion(S, 0, len(S) - 1, 0)

T = int(input())
for _ in range(T):
    S = input()
    a, b = isPalindrome(S)
    print(a, b)