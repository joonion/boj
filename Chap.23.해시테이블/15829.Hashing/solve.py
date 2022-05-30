def hash(S):
    r, M, a_ = 31, 1234567891, ord('a') - 1
    a = list(map(ord, list(S)))
    key = 0
    for i in range(len(a)):
        key += (a[i] - a_) * (r ** i)
    return key % M

L = int(input())
S = input()
hashkey = hash(S)
print(hashkey)