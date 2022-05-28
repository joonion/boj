'''
단순 로테이션 방식은 파이썬에서 시간 초과:
C 언어로 구현해서 시간 초과 문제를 해결
파이썬으로는 리스트 슬라이싱 방식을 사용함
'''

def rotate(k, N, M, R, A):
    cycle = []
    # add left line to the bottom
    for i in range(k, N-1-k):
        cycle.append(A[i][k])
    # add bottom line to the right
    for j in range(k, M-1-k):
        cycle.append(A[N-1-k][j])
    # add right line to the top
    for i in range(N-1-k, k, -1):
        cycle.append(A[i][M-1-k])
    # add top line to the left
    for j in range(M-1-k, k, -1):
        cycle.append(A[k][j])
    index = len(cycle) - R % len(cycle)
    rotated = cycle[index:] + cycle[:index]
    t = 0
    # add left line to the bottom
    for i in range(k, N-1-k):
        A[i][k] = rotated[t]
        t += 1
    # add bottom line to the right
    for j in range(k, M-1-k):
        A[N-1-k][j] = rotated[t]
        t += 1
    # add right line to the top
    for i in range(N-1-k, k, -1):
        A[i][M-1-k] = rotated[t]
        t += 1
    # add top line to the left
    for j in range(M-1-k, k, -1):
        A[k][j] = rotated[t]
        t += 1

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
for k in range(min(N, M) // 2):
    # k is an index from the outer cycle into the inner cycle
    rotate(k, N, M, R, A)
for i in range(len(A)):
    print(" ".join(map(str, A[i])))