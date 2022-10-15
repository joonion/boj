def recursion(S, low, high, cnt):
    if low >= high:
        return 1, cnt + 1
    elif S[low] != S[high]:
        return 0, cnt + 1
    else:
        return recursion(S, low + 1, high - 1, cnt + 1)
    
def isPalindrome(S):
    return recursion(S, 0, len(S) - 1, 0)

T = int(input())
for i in range(T):
    S = input()
    a, b = isPalindrome(S)
    print(a, b)