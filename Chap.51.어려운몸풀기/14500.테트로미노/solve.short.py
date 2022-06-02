import sys
input=sys.stdin.readline
def go(j,k,r,d,res):
  global opt
  if d==0:
    opt=max(opt,res)
  elif r<N:
    for s in range(1,d+1):
      for i in range(max(0,j-s+1),min(M-s+1,k)):
        go(i,i+s,r+1,d-s,res+sum(A[r][i:i+s]))

N,M=map(int,input().split())
A=[list(map(int,input().split()))for _ in range(N)]
opt=0
for r in range(N):
  go(0,M,r,4,0)
print(opt)