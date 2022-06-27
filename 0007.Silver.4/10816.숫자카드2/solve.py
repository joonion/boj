N = int(input())
n = map(int, input().split())
M = int(input())
m = map(int, input().split())

from collections import Counter
c = Counter(n)
for i in m:
    print(c[i], end=' ')

