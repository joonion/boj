def make_palindrome(s, u, v):
    if len(s) < 2:
        return u + v if len(s) == 0 else u + s + v
    elif s[0] == s[1]:
        return make_palindrome(s[2:], u + s[0], s[0] + v)
    elif len(s) > 2 and s[1] == s[2]:
        return make_palindrome(s[0] + s[3:], u + s[1], s[1] + v)
    else:
        return "I'm Sorry Hansoo"
        
def solve(s):
    s = "".join(sorted(s))
    print(make_palindrome(s, "", ""))
    
S = input()
solve(S)