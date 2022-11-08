N = int(input())
for i in range(N):
    print(f"Case #{i+1}:", end = " ")
    S = input().split()
    print(" ".join(S[::-1]))
    