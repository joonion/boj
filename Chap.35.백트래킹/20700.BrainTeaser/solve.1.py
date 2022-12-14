from itertools import permutations

def f(w, D):
    n = 0
    for c in w:
        n = n * 10 + D[c]
    return n

def is_valid(w1, w2, w3, D):
    if D[w1[0]] == 0 or D[w2[0]] == 0 or D[w3[0]] == 0:
        return False
    return f(w1, D) + f(w2, D) == f(w3, D)

def solve(w1, w2, w3, S):
    letters = list(set(w1 + w2 +w3))
    digits = list(range(10))
    for perm in permutations(digits, len(letters)):
        D = dict(zip(letters, perm))
        if is_valid(w1, w2, w3, D):
            if w3 not in solutions:
                solutions.append(w3)
            else:
                solutions.remove(w3); break
    
w1, w2 = input(), input()
solutions = []
for _ in range(int(input())):
    w3 = input()
    solve(w1, w2, w3, solutions)
print(len(solutions))
for s in solutions:
    print(s)