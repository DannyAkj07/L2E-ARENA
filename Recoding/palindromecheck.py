def is_palindrome(word: str) -> bool:
    if not word:
        return "Not a word"
    new_word = ""
    for char in word:
        if char.isalnum():
            new_word += char.lower()
    palindrome = ""
    for char in new_word:
        palindrome = char + palindrome
    # if palindrome == new_word:
    #     return True
    # else:
    #     return False
    return palindrome == new_word


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
