# def is_balanced(text) -> bool:
#     stack = []
#     balanced = {")": "(", "]": "[", "}": "{"}

#     for i in text:
#         if i in balanced.values():
#             stack.append(i)
#         elif i in balanced.keys():
#             if not stack:
#                 return False
#             elif stack[-1] == balanced[i]:
#                 stack.pop()
#             else:
#                 return False
#     return not stack


# print(is_balanced("()[]{}"))
# print(is_balanced("([{}])"))
# print(is_balanced("(]"))
# print(is_balanced("][]"))
# print(is_balanced(""))

def insertion_sort(nums):
    comparison = 0
    shift = 0

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0:
            comparison += 1
            if nums[j] > key:
                nums[j + 1] = nums[j]
                shift += 1
                j -= 1
            else:
                break
        nums[j + 1] = key
    return (comparison, shift)

print(insertion_sort([5,2,4,1]))
print(insertion_sort([1,2,3,4]))
print(insertion_sort([4,3,2,1]))
print(insertion_sort([]))
