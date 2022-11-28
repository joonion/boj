input();a=x=y=z=0
for b in map(int,input().split()):x=1+(b>=a)*x;y=1+(b<=a)*y;z=max(x,y,z);a=b
print(z)