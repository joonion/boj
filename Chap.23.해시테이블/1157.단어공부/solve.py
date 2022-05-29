def solve(word):
    word = word.upper()
    freq = [0] * 26
    for i in range(len(word)):
        j = ord(word[i]) - ord('A')
        freq[j] += 1
    best = max(freq)
    answer = -1
    for i in range(len(freq)):
        if freq[i] == best:
            if answer != -1:
                return '?'
            else:    
                answer = i
    return chr(ord('A') + answer)

word = input().strip()
answer = solve(word)
print(answer)