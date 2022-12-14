import itertools as i
while x:=input().split()[1:]:
 for y in i.combinations(x,6):print(" ".join(y))
 print()