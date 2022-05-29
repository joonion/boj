from math import floor, sqrt

def prepare_minfactor(n):
    minfactor = [i for i in range(n + 1)]
    for i in range(2, floor(sqrt(n)) + 1):
        for j in range(i * i, n + 1, i):
            if i < minfactor[j]:
                minfactor[j] = i
    return minfactor

def solve(n, minfactor):
    while n != 1:
        print(minfactor[n], end = " ")
        n = n // minfactor[n]
    print()

minfactor = prepare_minfactor(5000000)    
N = int(input())
nums = list(map(int, input().split()))
for i in range(N):
    solve(nums[i], minfactor)
   