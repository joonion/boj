def solve(n, s):
    low, high = 0, len(s) - 1
    cnt = 0
    while low < high:
        if s[low] != s[high]:
            cnt += 1
        low += 1
        high -= 1
    return cnt        
    
N = int(input())
S = input()
print(solve(N, S))