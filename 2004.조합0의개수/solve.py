def nfactor(x, f):
    cnt = 0
    while x >= f:
        cnt += x // f
        x //= f
    return cnt
    
def solve(n, m):
    '''
    끝자리 0의 개수 = n! / (n-m)! * m! 에서 소인수 2와 5의 지수 중에서 작은 것
    '''
    nf5 = nfactor(n, 5) - nfactor(n - m, 5) - nfactor(m, 5)
    nf2 = nfactor(n, 2) - nfactor(n - m, 2) - nfactor(m, 2)
    return min(nf5, nf2)
    
n, m = map(int, input().split())
answer = solve(n, m)
print(answer)