def solve(a, b, c):
    if a < b:
        if b < c: # c is largest
            if a < b: return b
            else: return a
        else: # b is largest
            if a < c: return c
            else: return a
    else:
        if a < c: # c is largest
            if a < b: return b
            else: return a
        else: # a is largest
            if b < c: return c 
            else: return b
        
A, B, C = map(int, input().split())
print(solve(A, B, C))