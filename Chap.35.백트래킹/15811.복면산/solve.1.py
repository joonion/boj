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

def solve(w1, w2, w3):
    letters = set(w1 + w2 + w3)
    digits = list(range(10))
    for p in permutations(digits, len(letters)):
        D = {k:v for k, v in zip(letters, p)}
        if is_valid(w1, w2, w3, D):
            print(to_int(w1, D))
            print(to_int(w2, D))
            print(to_int(w3, D))
            return True
    return False
    
w1, w2, w3 = input().split()
print("YES" if solve(w1, w2, w3) else "NO")