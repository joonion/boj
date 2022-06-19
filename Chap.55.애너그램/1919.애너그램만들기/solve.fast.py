a, b = input(), input()
d = [0] * 26
for c in a:
    d[ord(c) - 97] += 1
for c in b:
    d[ord(c) - 97] -= 1
s = 0
for i in range(26):
    s += abs(d[i])
print(s)