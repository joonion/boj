def to_arabic(roman):
    global tab1
    num = 0
    for i in range(len(roman)):
        if i < len(roman) - 1 and tab1[roman[i]] < tab1[roman[i+1]]:
            num -= tab1[roman[i]]
        else:
            num += tab1[roman[i]]
    return num

def to_roman(num):
    global tab2, tab3
    roman = ""
    for i in range(len(tab2)):
        while num >= tab2[i]:
            roman += tab3[i]
            num -= tab2[i]
    return roman

import re
def valid_roman(roman):
    regexp = r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return re.search(regexp, roman)

def solve(i, roman):
    global INF
    if i == len(roman) - 1:
        s = "".join(roman)
        return INF if not valid_roman(s) else to_arabic(s)
    else:
        minimum = INF
        for j in range(i, len(roman)):
            roman[i], roman[j] = roman[j], roman[i]
            minimum = min(minimum, solve(i + 1, roman))
            roman[i], roman[j] = roman[j], roman[i]
        return minimum
         
tab1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
tab2 = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
tab3 = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
INF = 100

B = list(input())
answer = solve(0, B)
print(to_roman(answer))

# print(valid_roman(0, 0, "IVI"))