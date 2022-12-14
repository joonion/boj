from itertools import permutations

def f(w, D):
    n = 0
    for i in range(len(w)):
        n += D[w[i]] * (10 ** i)
    return n

def promising(i, n, D, w1, w2, w3):
    print(i, n, D, w1, w2, w3)
    if i == 0: return True
    a = f(w1[:i], D)
    b = f(w2[:i], D)
    c = f(w3[:i], D)
    M = 10 ** i
    return (a + b) % M == c % M

def ith_letters(i, w1, w2, w3, D):
    s = ""
    if i < len(w1): s += w1[i]
    if i < len(w2): s += w2[i]    
    if i < len(w3): s += w3[i]
    return set(s) - set(D.keys())
    
def backtrack(i, n, D, w1, w2, w3):
    global solutions
    if promising(i, n, D, w1, w2, w3):
        if i == n:
            if D[w1[-1]] != 0 and D[w2[-1]] != 0 and D[w3[-1]] != 0:
                solutions.append(w3)
        else:
            letters = ith_letters(i, w1, w2, w3, D)
            digits = set(range(10)) - set(D.values())
            for perm in permutations(digits, len(letters)):
                for k, v in zip(letters, perm): D[k] = v
                backtrack(i + 1, n, D, w1, w2, w3)
                for k in letters: D.pop(k)
            
def solve(w1, w2, w3):
    n = max(len(w1), len(w2), len(w3))
    backtrack(0, n, {}, w1, w2, w3)

w1, w2 = input()[::-1], input()[::-1]
solutions = []
for _ in range(int(input())):
    w3 = input()[::-1]
    solve(w1, w2, w3)
print(len(solutions))
print("\n".join(solutions))
