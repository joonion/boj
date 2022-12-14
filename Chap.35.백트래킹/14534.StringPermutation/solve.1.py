from itertools import permutations

for i in range(int(input())):
    print(f"Case # {i+1}:")
    perms = permutations(input())
    for p in perms:
        print("".join(p))