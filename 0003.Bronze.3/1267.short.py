a,b=open(0)
y,m=0,0
for t in map(int,b.split()):y+=t//30*2+2;m+=t//60*3+3
print('Y'if y<m else 'M'if y>m else'Y M',min(y,m)*5)
