from math import floor, sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, floor(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def solve(nums):
    count = 0
    for i in range(len(nums)):
        if is_prime(nums[i]):
            count += 1
    return count
   
N = int(input())
nums = list(map(int, input().split()))
answer = solve(nums)
print(answer)
    
