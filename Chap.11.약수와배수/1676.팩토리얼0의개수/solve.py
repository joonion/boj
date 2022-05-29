def nfactor(x, f):
    cnt = 0
    while x >= f:
        cnt += x // f
        x //= f
    return cnt
    
def solve(n):
    '''
    끝자리 0의 개수 = n! 에서 소인수 2와 5의 지수 중에서 작은 것
    '''
    return min(nfactor(n, 2), nfactor(n, 5))
    
n = int(input())
answer = solve(n)
print(answer)