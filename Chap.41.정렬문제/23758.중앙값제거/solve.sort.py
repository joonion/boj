import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))
S.sort()
median = S[(N - 1) // 2]
print(median)
cnt = 0
while median > 0:
    cnt += 1
    median //= 2
    print(median)
print(cnt)
