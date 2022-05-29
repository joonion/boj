from math import floor, sqrt

def solve(n, k):
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0
    kth = 0
    # for i in range(2, floor(sqrt(n)) + 1):
    for i in range(2, n + 1):
        '''
        문제의 조건에서 처음 만나는 소수도 지워진 것으로 보기 때문에
        모든 소수를 만날 때까지 for-loop를 순회해야 함.
        원래는 floor(sqrt(n))까지 돌면 남은 것은 모두 소수임.
        '''
        if sieve[i] == 1:
            kth += 1
            if kth == k:
                return i
            for j in range(i * i, n + 1, i):
                if sieve[j] == 1:
                    kth += 1
                    if kth == k:
                        return j
                sieve[j] = 0
    
N, K = map(int, input().split())
answer = solve(N, K)
print(answer)
