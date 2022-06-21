s = input()
S = ""
for c in s:
    S += c.lower() if c.isupper() else c.upper()
print(S)
