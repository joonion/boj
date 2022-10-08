def dist(cx, cy, nx, ny):
    dx, dy = cx - nx, cy - ny
    if dx * dy >= 0:
        return abs(dx + dy) - min(abs(dx), abs(dy))
    else:
        return abs(dx) + abs(dy)

w, h, n = map(int, input().split())
cnt = 0
cx, cy = map(int, input().split())
for _ in range(n - 1):
    nx, ny = map(int, input().split())
    cnt += dist(cx, cy, nx, ny)
    cx, cy = nx, ny
print(cnt)
