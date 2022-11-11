from math import ceil
n = int(input())
cnt = 0
for x in range(ceil(n/3), ceil(n/2)):
    cnt += x - ceil((n-x)/2) + 1
print(cnt)