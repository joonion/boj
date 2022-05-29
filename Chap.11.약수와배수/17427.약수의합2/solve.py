'''
N 이하의 모든 수 i, k = 1, 2, ..., N 에 대해서
i의 약수들의 집합에서 k가 나타나는 패턴을 관찰
(N/1)은 1번, (N/2)는 2번 (N/3)은 3번 ... (N/N)은 N번
'''

N = int(input())
g = 0
for i in range(1, N + 1):
    g += (N // i) * i
print(g)
    