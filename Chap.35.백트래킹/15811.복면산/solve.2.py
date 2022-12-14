from itertools import permutations 

def to_int(w, D):
    n = 0
    for i, c in enumerate(w[::-1]):
        n += D[c] * (10 ** i)
    return n

def is_valid(w1, w2, w3, D):
    if D[w1[0]] == 0 or D[w2[0]] == 0 or D[w3[0]] == 0:
        return False
    return to_int(w1, D) + to_int(w2, D) == to_int(w3, D)

def promising(i, map, s1, s2, s3):
    n = 10 ** (i + 1)
    a = to_int(s1[::-1], map)
    b = to_int(s2[::-1], map)
    c = to_int(s3[::-1], map)
    return (a + b) % n == c % n

def ith(i, s1, s2, s3):
    s = ""
    if i < len(s1): s += s1[i]
    if i < len(s2): s += s2[i]
    if i < len(s3): s += s3[i]
    return set(s)

def solveto(n, i, map, solved, r1, r2, r3):
    if i == n:
        if is_valid(r1[::-1], r2[::-1], r3[::-1], map):
            solved.append(map.copy())
    else:
        s1, s2, s3 = r1[:(i+1)], r2[:(i+1)], r3[:(i+1)]
        letters = ith(i, s1, s2, s3) - set(map.keys())
        digits = set(range(10)) - set(map.values())
        perms = list(permutations(digits, len(letters)))
        for perm in perms:
            for k, v in zip(letters, perm):
                map[k] = v
            if promising(i, map, s1, s2, s3):
                solveto(n, i + 1, map, solved, r1, r2, r3)
            for k in letters:
                map.pop(k)

def solve(w1, w2, w3):
    r1, r2, r3 = w1[::-1], w2[::-1], w3[::-1]
    n = max(len(w1), len(w2), len(w3))
    map, solved = {}, []
    solveto(n, 0, map, solved, r1, r2, r3)
    return solved
    
w1, w2, w3 = input().split()
print("YES" if solve(w1, w2, w3) else "NO")