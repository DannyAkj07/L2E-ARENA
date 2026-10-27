def is_valid_parenthesis(s: str) -> bool:
    matched = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)  
        elif stack[-1] == matched[char]:
            stack.pop()
        else:
            return False
    return not stack
        
print(is_valid_parenthesis("()[]{}"))
print(is_valid_parenthesis("([{}])"))
print(is_valid_parenthesis("(]"))
# print(is_valid_parenthesis("][]"))