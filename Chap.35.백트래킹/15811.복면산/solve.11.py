from itertools import permutations

def f(w, D):
    n = 0
    for c in w:
        n = n * 10 + D[c]
    return n

def solve(w1, w2, w3):
    letters = set(w1 + w2 + w3)
    if len(letters) > 10: return False
    numbers = list(range(10))
    for perm in permutations(numbers, len(letters)):
        D = dict(zip(letters, perm))
        if D[w1[0]] == 0 or D[w2[0]] == 0 or D[w3[0]] == 0:
            continue
        if f(w1, D) + f(w2, D) == f(w3, D):
            return True
    return False

w1, w2, w3 = input().split()
print("YES" if solve(w1, w2, w3) else "NO")