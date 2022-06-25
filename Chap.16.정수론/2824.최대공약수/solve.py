n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
a = 1
for i in A:
    a *= i
b = 1
for i in B:
    b *= i

from math import gcd
s = str(gcd(a, b))
if len(s) > 9:
    s = s[len(s)-9:len(s)]
print(s)
