def is_balanced(text) -> bool:
    if not text:
        return True
    stack = []
    balanced = {")": "(", "]": "[", "}": "{", }

    for i in text:
        if i in balanced.values():
            stack.append(i)
        elif i in balanced:
            if not stack:
                return False
            elif stack[-1] == balanced[i]:
                stack.pop()
            else:
                return False
    return not stack


print(is_balanced("(a + b) * [c - d]"))
print(is_balanced("{[()]}"))
print(is_balanced("([)]"))
print(is_balanced("(("))
print(is_balanced(")("))
print(is_balanced(""))
