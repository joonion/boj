n, m = map(int, input().split())
A = list(map(int, input().split()))

largest = 0

from itertools import combinations
comb = combinations(A, 3)
for c in comb:
    s = sum(list(c))
    if s <= m:    
        largest = max(largest, s)
print(largest)