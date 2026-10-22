def reverse_string(word: str) -> str:
    if not word:
        return "Not a word"
    reverse = ""
    for char in word:
        reverse = char + reverse
    return reverse


print(reverse_string('Data Science'))
