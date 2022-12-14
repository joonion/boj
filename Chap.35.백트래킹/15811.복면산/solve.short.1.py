from itertools import*
p=print
A,B,C=input().split()
K=len(L:=set(A+B+C))
if K>10:exit(p("NO"))
def t(A,B,C,o,n):
 for i in zip(o,n):A=A.replace(*i);B=B.replace(*i);C=C.replace(*i)
 return A,B,C
for i in permutations("0123456789",K):
 a,b,c=map(int,t(A,B,C,L,i))
 if a+b==c:exit(p("YES"))
p("NO")