T = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def to_arabic(r):
    n = 0
    for i in range(len(r)):
        if i < len(r) - 1 and T[r[i]] < T[r[i+1]]:
            n -= T[r[i]]
        else:
            n += T[r[i]]
    return n

print(to_arabic(input()))
        