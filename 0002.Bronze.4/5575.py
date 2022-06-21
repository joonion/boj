def timestamp(h, m, s):
    return h * 60 * 60 + m * 60 + s

def time(t):
    return t // 3600, (t // 60) % 60, t % 60

for _ in range(3):
    a, b, c, d, e, f = map(int, input().split())
    h, m, s = time(timestamp(d, e, f) - timestamp(a, b, c))
    print(h, m, s)