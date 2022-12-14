from itertools import*
a,b=input().split()
c=[i for i in map("".join,set(permutations(a)))if i[0]!='0'and int(i)<int(b)]
print(max(c)if c else -1)