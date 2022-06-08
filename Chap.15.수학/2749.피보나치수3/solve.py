n = int(input())
m = 1000000
p = m // 10 * 15
if n < 2:
    print(n)
else:
    a, b = 0, 1
    for i in range(2, n % p + 1):    
        a, b = b, (a + b) % 1000000
    print(b)