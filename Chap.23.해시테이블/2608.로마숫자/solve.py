T1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
T2 = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}

def to_arabic(r):
    n = 0
    for i in range(len(r)):
        if i < len(r) - 1 and T1[r[i]] < T1[r[i+1]]:
            n -= T1[r[i]]
        else:
            n += T1[r[i]]
    return n

def to_roman(n):
    nums = list(T2.keys())
    strs = list(T2.values())
    r = ""
    for i in range(len(T2)):
        while n >= nums[i]:
            r += strs[i]
            n -= nums[i]
    return r

A, B = input(), input()
C = to_arabic(A) + to_arabic(B)
print(C)
print(to_roman(C))