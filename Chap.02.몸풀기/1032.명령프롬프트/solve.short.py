p=''
for x in zip(*[*open(0)][1:]):p+='?'if len({*x})>1 else x[0]
print(p)