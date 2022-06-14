S = input().strip()
T = [-1] * 26
for i in range(len(S)):
    pos = ord(S[i]) - ord('a')
    if T[pos] < 0:
        T[pos] = i
print(" ".join(map(str, T)))

    