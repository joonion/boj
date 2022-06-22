def solve(n):
    s = list(map(int, list(str(n))))
    zero = s.count(0)
    one = s.count(1)
    return len(s) + 1 + zero*4 + one*2 + (len(s)-zero-one)*3
    
while True:
    n = int(input())
    if n == 0: break
    print(solve(n))