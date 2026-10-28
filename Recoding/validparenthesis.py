def is_valid_parenthesis(s: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in s:
        # if char in "([{":
        # if char == "(" or char == "[" or char == "{":
        if char in pairs.values():
            stack.append(char)

        # if char in ")]}":
        # if char == ")" or char == "]" or char == "}":
        # if char in pairs.keys:
        elif char in pairs:
            if not stack:
                return False
            elif stack[-1] == pairs[char]:
                stack.pop()
            else:
                return False

    return not stack


print(is_valid_parenthesis("()[]{}"))
print(is_valid_parenthesis("([{}])"))
print(is_valid_parenthesis("(]"))
print(is_valid_parenthesis("][]"))
