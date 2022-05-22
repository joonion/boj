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

def solve(num):
    if num.isdigit():
        return to_roman(int(num))
    else:
        return to_arabic(num)

tab1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
tab2 = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
tab3 = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

T = int(input())
for _ in range(T):
    num = input()
    answer = solve(num)
    print(answer)
