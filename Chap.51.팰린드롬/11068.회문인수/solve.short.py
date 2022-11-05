for x in[0]*int(input()):
 n=int(input())
 for b in range(2,65):
  m=n;d=[]
  while m:d+=[m%b];m//=b
  x|=d==d[::-1]
 print(x)