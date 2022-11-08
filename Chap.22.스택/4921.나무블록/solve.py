def valid(i, j):
    if i == 1:
        return j in [4, 5]
    elif i == 2:
        return False
    elif i == 3:
        return j in [4, 5]
    elif i == 4:
        return j in [2, 3]
    elif i == 5:
        return j == 8
    elif i == 6:
        return j in [2, 3]
    elif i == 7:
        return j == 8
    elif i == 8:
        return j in [6, 7]

def solve(B):
    b = list(map(int, B))
    if b[0] != 1 or b[-1] != 2:
        return False
    for i in range(1, len(B) - 1):
        if not valid(b[i-1], b[i]) or not valid(b[i], b[i+1]):
            return False
    return True

i = 1
while True:
    B = input()
    if (B == '0'): break
    print(f"{i}. VALID" if solve(B) else f"{i}. NOT")
    i += 1
