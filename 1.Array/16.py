def romanToInt(s):
    translations = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    total = 0
    prevValue = 0

    for char in reversed(s):
        currentValue = translations[char]
        if currentValue < prevValue:
            total -= currentValue
        else:
            total += currentValue
        prevValue = currentValue

    return total
s = "MCMXCIV"
print(romanToInt(s))