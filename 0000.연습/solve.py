N = int(input())
S = list(map(int, input().split()))
S2 = [S[i]/max(S) for i in range(N)]
print(sum(S2)/N*100)

# A, B = map(int, input().split())
# if A > B:
#     print('>')
# elif A < B:
#     print('<')
# else:
#     print('==')

# print(len(input().split()))