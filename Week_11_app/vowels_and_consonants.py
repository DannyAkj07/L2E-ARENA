def count_letters(text):
    vowel = "aeiou"
    vowels = 0
    consonants = 0
    for i in text.lower():
        # if i >= "a" and i <= "z":
        if "a" <= i <= "z":
            if i in vowel:
                vowels += 1
            else:
                consonants += 1
    return (vowels, consonants)



print(count_letters("Hello, World 123"))
print(count_letters("AEIOU"))
print(count_letters("rhythm"))
print(count_letters(""))
print(count_letters("12345!@#"))
print(count_letters("Python 3.12"))
