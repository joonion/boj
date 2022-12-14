from itertools import permutations

def f(r, D):
    n = 0
    for i in range(len(r)):
        n += D[r[i]] * (10 ** i)
    return n

def promising(i, n, D, s1, s2, s3):
    # print(i, n, D, s1, s2, s3)
    if i == 0: return True
    a, b, c = f(s1, D), f(s2, D), f(s3, D)
    M = 10 ** i
    return (a + b) % M == c % M

def ith_letters(i, r1, r2, r3, D):
    s = ""
    if i < len(r1): s += r1[i]
    if i < len(r2): s += r2[i]
    if i < len(r3): s += r3[i]
    return set(s) - set(D.keys())

def ith_digits(D):
    return set(range(10)) - set(D.values())

def backtrack(i, n, D, r1, r2, r3):
    if promising(i, n, D, r1[:i], r2[:i], r3[:i]):
        if i > n:
            exit(print("YES"))
        else:
            letters = ith_letters(i, r1, r2, r3, D)
            digits = ith_digits(D)
            for perm in permutations(digits, len(letters)):
                for k, v in zip(letters, perm):
                    D[k] = v
                backtrack(i + 1, n, D, r1, r2, r3)
                for k in letters:
                    D.pop(k)
        
def solve(r1, r2, r3):
    n = max(len(r1), len(r2), len(r3))
    backtrack(0, n, {}, r1, r2, r3)
    print("NO")

w1, w2, w3 = input().split()
solve(w1[::-1], w2[::-1], w3[::-1])
