def roman(s: str) -> int:
    group = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    count = 0
    for i in range(len(s)):
        current_value = group[s[i]]
        if i + 1 < len(s) and current_value < group[s[i + 1]]:
            count -= current_value
        else:
            count += current_value
    return count

print(roman("LVIII"))
print(roman("III"))
print(roman("MCMXCIV"))