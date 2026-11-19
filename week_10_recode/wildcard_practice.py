def is_match(text, pattern):
    if not pattern and not text:
        return True
    if not pattern and text:
        return False
    if text == "":
        if pattern[0] == "*":
            return is_match(text, pattern[1:])
        return False
    if pattern[0] == "*":
        return is_match(text, pattern[1:]) or is_match(text[1:], pattern)
    if pattern[0] == "?" or pattern[0] == text[0]:
        return is_match(text[1:], pattern[1:])
    return False


print(is_match("helloworld", "h*d"))
print(is_match("bad", "b?d"))
print(is_match("cat", "c*t?"))
print(is_match("cat", "c?t*"))
