# def vowels(word: str) -> int:
#     word = word.lower()
#     if not word:
#         return "Not a word"
#     count = 0
#     for item in word:
#         if "a" == item or "e" == item or "i" == item or "o" == item or "u" == item:
#             count += 1

#     return count


# print(vowels("PYTHON programming"))

def vowels(word: str) -> bool:
    if not word:
        return "Not a word"
    vowel = "aeiou"
    count = 0
    for item in word.lower():
        if item in vowel:
            count += 1
    return count


print(vowels("PYTHON programming"))
