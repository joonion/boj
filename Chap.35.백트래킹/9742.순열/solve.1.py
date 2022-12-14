from itertools import permutations

def solve(s, k):
    for i, p in enumerate(permutations(s), start = 1):
        if i == k:
            print(f"{s} {k} = {''.join(p)}")
            break
    else:
        print(f"{s} {k} = No permutation")
        
while True:
    try:
        s, k = input().split()
        solve(s, int(k))
    except:
        break
    