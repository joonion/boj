o="({[";c=")}]"
for s in[*open(0)][:-1]:
 t=[];l=1
 for x in s:
  if x in o:t+=x
  if x in c and (not t or c.index(x)!=o.index(t.pop())):l=0
 print("Illegal"if not l or t else"Legal")