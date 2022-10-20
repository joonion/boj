W=open(0).read().split()
H={}
for w in W:s="".join(sorted(w));H.setdefault(s,[]).append(w)
for k in H:H[k].sort()
S=sorted(H.values(),key=lambda x:(-len(x),x[0]))
for s in S[:5]:print(f"Group of size {len(s)}: {' '.join(sorted(set(s)))} .")