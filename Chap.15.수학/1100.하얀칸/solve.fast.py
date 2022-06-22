s = ""
for _ in range(8):
    s += input() + ' '
print(s[::2].count('F'))