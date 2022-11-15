def hash(S):
    r, M = 31, 1234567891
    a = list(map(ord, list(S)))
    key = 0
    for i in range(len(a)):
        key += (a[i] - ord('a') + 1) * (r ** i)
    return key % M

L = int(input())
S = input()
hashkey = hash(S)
print(hashkey)