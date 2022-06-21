a, b, c = list(map(int, input().split()))
d = int(input()) + a * 60 * 60 + b * 60 + c
print((d // 3600) % 24, (d // 60) % 60, d % 60)
