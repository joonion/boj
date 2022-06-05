def g(i,j,L,R):
 if i==n-1 and j==m-1:return 1
 for t in range(7):
  x,l,r=D.index(A[i][j]),L,R
  if 1<=t<=3:x=(x-t)%4;l=L-t
  elif 4<=t<=6:x=(x+t-3)%4;r=R-t+3
  p,q=i+a[x],j+b[x]
  if 0<=p<n and 0<=q<m and M[p][q]==0 and l>=0 and r>=0:
   M[p][q]=1
   if g(p,q,l,r):return 1
   M[p][q]=0
 return 0

D,a,b="URDL",[-1,0,1,0],[0,1,0,-1]
n,m,k=map(int,input().split())
A=[input() for _ in range(n)]
M=[[0]*m for _ in range(n)]
M[0][0]=1
print("Yes" if g(0,0,k,k) else "No")