from math import sqrt

def guess(x, y, w):
    hx = sqrt(x**2 - w**2)
    hy = sqrt(y**2 - w**2)
    return hx * hy / (hx + hy)

def binsearch(x, y, c):
    low, high = 0, min(x, y)
    while high - low > 0.0001:
        mid = (low + high) / 2
        if guess(x, y, mid) >= c:
            low = mid 
        else:
            high = mid
    return low

x, y, c = map(float, input().split())
ret = binsearch(x, y, c)
print(f"{ret:.3f}")