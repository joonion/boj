h, m = map(int, input().split())
if m < 45:
    h = 23 if h == 0 else h - 1
print(h , (m - 45) % 60)