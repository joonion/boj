n = int(input())
cnt = 0
for x in range(1, n):
    for y in range(x, n):
        z = n - x - y
        if y <= z and x + y > z:
            cnt += 1
print(cnt)