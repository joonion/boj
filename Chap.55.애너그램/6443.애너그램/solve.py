def anagram(i, s):
    if i == len(s):
        print("".join(s))
    else:
        anagram(i + 1, s)
        for j in range(i + 1, len(s)):
            if s[i] != s[j]:
                s[i], s[j] = s[j], s[i]
                anagram(i + 1, s)
            
def solve(s):
    s = sorted(s)
    anagram(0, s)
    
for _ in range(int(input())):
    s = input()
    solve(s)