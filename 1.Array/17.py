def intToRoman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman = ""

    for i in range(len(values)):
        while num >= values[i]:
            num -= values[i]
            roman += symbols[i]

    return roman

num = 1994
print(intToRoman(num))