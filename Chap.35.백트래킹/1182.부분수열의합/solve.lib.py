from itertools import combinations

def solve(n, s, A):
    cnt = 0
    for i in range(1, n + 1):
        comb = combinations(A, i)
        for c in comb:
            if sum(c) == s:
                cnt += 1
    return cnt

n, s = map(int, input().split())
A = list(map(int, input().split()))
print(solve(n, s, A))
