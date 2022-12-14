import itertools as i
for c in range(int(input())):print(f"Case # {c+1}:\n"+"\n".join(["".join(p)for p in i.permutations(input())]))