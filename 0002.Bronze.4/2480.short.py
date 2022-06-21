p=print
a,b,c=sorted(list(map(int,input().split())))
if a==b:
 if b==c:p(10000+a*1000)
 else:p(1000+a*100)
elif b==c:p(1000+b*100)
else:p(c*100)
