a,*b=map(int,open(0))
s=[];o="";j=0
for i in range(a):
 s+=[i+1];o+="+\n"
 while s and b[j]==s[-1]:s.pop();o+="-\n";j+=1
print("NO"if s else o)