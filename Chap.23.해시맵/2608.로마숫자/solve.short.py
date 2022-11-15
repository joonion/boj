d=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
def t(n):
 r=''
 for i in range(13):
  while n>=d[i]:j=i+i//2;r+='MCMDCDCXCLXLXIXVIVI'[j:j+1+i%2];n-=d[i]
 return r
f={t(i):i for i in range(1,4000)}
print(s:=f[input()]+f[input()])
print(t(s))