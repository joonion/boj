S = int(input())
cnt, i = 0, 1
while True:
    S -= i
    cnt += 1
    i += 1
    if S < 0: break
print(cnt - 1)