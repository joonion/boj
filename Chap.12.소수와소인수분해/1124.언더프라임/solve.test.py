def num_factor(n):
    if n <= 1: return 0
    cnt = 0
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            cnt += 1
            n //= i
    cnt += n != 1
    return cnt

maxval = 0
for i in range(2, 100001):
    maxval = max(maxval, num_factor(i))
print(maxval)
    