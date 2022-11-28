j=1;s=[0];o=""
for i in[*map(int,open(0))][1:]:
 if s[-1]>i:o="NO";break
 while j<=i:s+=[j];j+=1;o+="+\n"
 s.pop();o+="-\n"
print(o)