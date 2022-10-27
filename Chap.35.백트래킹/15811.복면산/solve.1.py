from itertools import permutations

def to_int(w, D):
    c = list(w[::-1])
    n = 0
    for i in range(len(c)):
        n += D[c[i]] * (10**i)
    return n

def is_valid(D, w1, w2, w3):
    n1 = to_int(w1, D)
    n2 = to_int(w2, D)
    n3 = to_int(w3, D)
    return n1 + n2 == n3

def solve(w1, w2, w3):
    letters = set(w1 + w2 + w3)
    digits = [i for i in range(10)]
    perms = permutations(digits, len(letters))
    cnt = 0
    for perm in perms:
        D = {k:v for k, v in zip(letters, perm)}
        if is_valid(D, w1, w2, w3):
            cnt += 1
    return cnt    
    
w1, w2, w3 = input().split()
print("YES" if solve(w1, w2, w3) else "NO")