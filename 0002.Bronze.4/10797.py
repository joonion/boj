day = int(input())
num = list(map(int, input().split()))
cnt = 0
for n in num:
    cnt += (n == day)
print(cnt)