from collections import Counter

a, b = input(), input()
c, d = Counter(a), Counter (b)
cnt = 0
for key in c.keys():
    if key in d:
        cnt += abs(c[key] - d[key])
        d[key] = 0
    else:
        cnt += c[key]
for key in d.keys():
    cnt += d[key]
print(cnt)        
