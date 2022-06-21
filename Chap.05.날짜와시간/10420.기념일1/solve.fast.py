y, m, d = 2014, 4, 1
D = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days(y, m):
    if m == 2 and ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
        return 29
    return D[m]

n = int(input())
while n > 0:
    x = days(y, m)
    if n + d <= x:
        d += n; break
    m += 1
    n -= x
    
print(f'{y}-{m:02d}-{d:02d}')