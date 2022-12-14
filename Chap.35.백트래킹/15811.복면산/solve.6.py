from itertools import permutations

def to_int(word, T):
    n = 0
    for c in word:
        n = n * 10 + T[c]
    return n

def promising(i, n, T, S, w):
    if w[0][0] in T and T[w[0][0]] == 0:
        return False
    if w[1][0] in T and T[w[1][0]] == 0:
        return False
    if w[2][0] in T and T[w[2][0]] == 0:
        return False
    if i > 0:
        a = to_int(w[0][-i:], T)
        b = to_int(w[1][-i:], T)
        c = to_int(w[2][-i:], T)
        M = 10 ** i
        if (a + b) % M != c % M:
            return False
    return True

def ith(i, w):
    s = ""
    if i < len(w[0]): s += w[0][-(i+1)]
    if i < len(w[1]): s += w[1][-(i+1)]
    if i < len(w[2]): s += w[2][-(i+1)]
    return s

def backtrack(i, n, T, S, w):
    if promising(i, n, T, S, w):
        if i == n:
            S.append(T.copy())
            exit(print("YES"))
        else:
            letters = set(ith(i, w)) - set(T.keys())
            digits = set(range(10)) - set(T.values())
            for p in permutations(digits, len(letters)):
                for key, value in zip(letters, p):
                    T[key] = value
                backtrack(i + 1, n, T, S, w)
                for key in letters:
                    T.pop(key)

def solve(w):
    letters = sorted(set(w[0] + w[1] + w[2]))
    if len(letters) > 10: return False
    n = max(len(w[0]), len(w[1]), len(w[2]))
    T, S = {}, []
    backtrack(0, n, T, S, w)
    return S
    
words = input().split()
print("YES" if solve(words) else "NO")
