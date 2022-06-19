cnt = []
maxm = 0
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    cnt.append([n, m, 0])
    maxm = max(maxm, m)
    
a, b = 1, 2
while a <= maxm:
    for i in range(len(cnt)):
        if cnt[i][0] <= a <= cnt[i][1]:
            cnt[i][2] += 1
    a, b = b, a + b
for i in range(len(cnt)):
    print(cnt[i][2])