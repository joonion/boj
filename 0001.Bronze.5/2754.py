H = {'A':4, 'B':3, 'C':2, 'D':1, 'F':0}
L = {'+':.3, '0':.0, '-':-.3}
g = input()
if g == "F": print(0.0)
else: print(H[g[0]]+L[g[1]])