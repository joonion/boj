def solve(n):
    cnt = 0
    for i in range(len(c)):
        while n >= c[i]:
            n -= c[i]
            cnt += 1
        if n == 0: break
    return cnt
            
c = [500, 100, 50, 10, 5, 1]
n = int(input())
print(solve(1000 - n))