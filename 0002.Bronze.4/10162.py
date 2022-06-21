t = int(input())
if t % 10 != 0:
    print(-1)
else:
    print(t // 300, (t // 60) % 5, (t // 10) % 6)