e=[0,1,0,-1]
f=[1,0,-1,0]
a,*A=open(0)
N,M=map(int,a.split())
Q=[(0,1)]
V=[1]*(N*M)
V[0]=0
X=9**9
while Q:
 u,d=Q.pop(0)
 if u==N*M-1:
  X=min(X,d)
 for k in range(4):
  x,y=(u//M)+e[k],(u%M)+f[k]
  if 0<=x<N and 0<=y<M and A[x][y]=="1" and V[x*M+y]:
   Q+=[(x*M+y,d+1)]
   V[x*M+y]=0
print(X)