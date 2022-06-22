n = int(input())
A = [input()[0] for _ in range(n)]
B = sorted(list(set(A)))
found = False
for c in B:
    if A.count(c) > 4: print(c, end=''); found = True
if not found:
    print("PREDAJA")
