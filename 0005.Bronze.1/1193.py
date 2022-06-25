x = int(input())
a, n = 1, 1
while a + n <= x:
    a += n
    n += 1
if n % 2 == 1:
    print(f"{a + n - x}/{x - a + 1}")
else:
    print(f"{x - a + 1}/{a + n - x}")