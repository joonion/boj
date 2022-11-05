def solve(n):
    cnt = 0
    for c in range((n+1)//3, (n+1)//2):
        cnt += (3*c-n+2)//2
    return cnt

N = int(input())
print(solve(N))