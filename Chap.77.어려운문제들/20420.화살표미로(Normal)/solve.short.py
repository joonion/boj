a=[-1,0,1,0]
b=[0,1,0,-1]
n,m,k=map(int,input().split())
A=[[0]*m for _ in range(n)]
for i in range(n):
 s=input()
 for j in range(m):
  A[i][j]="URDL".index(s[j])
M=[[[151]*151 for _ in range(m)] for _ in range(n)]
Q=[(0,0,0,0)]
M[0][0][0]=0
while Q:
 i,j,l,r=Q.pop(0)
 for t in range(7):
  x,L,R=A[i][j],l,r
  if 0<t<4:x=(x-t)%4;L+=t
  if 3<t<7:x=(x+t-3)%4;R+=t-3
  I,J=i+a[x],j+b[x]
  if 0<=I<n and 0<=J<m and L<=k and R<=k and M[I][J][L]>R:
   if I==n-1 and J==m-1:print("Yes");exit(0)
   Q.append((I,J,L,R));M[I][J][L]=R
print("No")