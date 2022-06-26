a, b, n = map(int, input().split())

for i in range(n):
    a = (a % b) * 10
    c = a // b
print(c)
