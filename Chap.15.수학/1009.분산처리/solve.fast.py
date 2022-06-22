import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    x = a % 10
    y = (b - 1) % [1, 1, 4, 4, 2][x % 10 % 5] + 1
    z = x ** y % 10
    print(10 if z == 0 else z)