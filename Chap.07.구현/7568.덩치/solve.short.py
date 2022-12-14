x,*y=open(0);z=[[*map(int,i.split())]for i in y]
for a,b in z:print(1+sum((a<c)*(b<d)for c,d in z))