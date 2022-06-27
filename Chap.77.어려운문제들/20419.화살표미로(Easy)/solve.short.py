def s(v,l,r):
 if v==e:return 1
 for t in range(3):
  i,j=v//m,v%m;x,L,R=b.index(A[i][j]),l,r
  if t==1:x=(x-1)%4;L+=1
  if t>1:x=(x+1)%4;R+=1
  p,q=i+c[x],j+d[x];u=p*m+q
  if 0<=p<n and 0<=q<m and M[u] and L<=k and R<=k:
   M[u]=0
   if s(u,L,R):return 1
   M[u]=1
a,*A=open(0)
n,m,k=map(int,a.split())
b,c,d,e="URDL",[-1,0,1,0],[0,1,0,-1],n*m-1
M=[0]+[1]*e
print("Yes"if s(0,0,0)else"No")