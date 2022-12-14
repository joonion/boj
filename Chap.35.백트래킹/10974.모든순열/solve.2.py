def perm(i, n, s):
    if i == n:
        print("".join(s))
    else:
        for j in range(i, n):
            s[i], s[j] = s[j], s[i]
            perm(i + 1, n, s)
            s[i], s[j] = s[j], s[i]

from string import ascii_uppercase
N = int(input())
S = ascii_uppercase[:N]
perm(0, N, S)