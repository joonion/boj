a, b = map(int, input().split())
S, i = [], 1
while len(S) < 1000:
    S += [i] * i
    i += 1
print(sum(S[a-1:b]))