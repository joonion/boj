from itertools import*
p=print
def f(a,b,c,d):
 for i in d:a=a.replace(*i);b=b.replace(*i);c=c.replace(*i)
 return a,b,c
a,b,c=input().split()
k=len(l:=set(a+b+c))
if k>10:exit(p("NO"))
for x in permutations("0123456789",k):
 A,B,C=map(int,f(a,b,c,zip(l,x)))
 if A+B==C:exit(p("YES"))
p("NO")