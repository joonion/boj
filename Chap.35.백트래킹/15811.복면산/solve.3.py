from itertools import permutations

def solve(w1, w2, w3):
    letters = set(w1 + w2 + w3)
    if len(letters) > 0:
        return False
    


w1, w2, w3 = input().split()
print("Yes" if solve(w1, w2, w3) else "No")
