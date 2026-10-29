# def sum_nested_list(nested_list: list) -> int:
#     if not nested_list:
#         return []

#     total = 0
#     for item in nested_list:
#         if isinstance(item,list):
#             total += sum_nested_list(item)
#         else:
#             total += item
#     return total

# print(sum_nested_list([1, [2, 3], [4, [5]]]))

def is_valid_parenthesis(s: str) -> bool:
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack:
                return False
            if pairs[char] == stack[-1]:
                stack.pop()
            else:
                return False
    # return not stack
    # ====== OR ======

    # return len(stack) == 0
    # ====== OR ======

    if len(stack) == 0:
        return True
    else:
        return False


print(is_valid_parenthesis("(){}[]"))
print(is_valid_parenthesis("([{}])"))
print(is_valid_parenthesis("]"))
