days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isleap(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

def invalid(y, m, d):
    if m == 2 and isleap(y):
        return d > 29
    return d > days[m - 1]

y, m, d = 2014, 4, 2
n = int(input())
for _ in range(n - 1):
    d += 1
    if invalid(y, m, d):
        d = 1
        m += 1
        if m > 12:
            m = 1
            y += 1
print(f"{y}-{m:02d}-{d:02d}")
