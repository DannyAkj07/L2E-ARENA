def insert_bottom(stack, item):
    if stack == []:
        stack.append(item)
        return

    else:
        top = stack.pop()
        insert_bottom(stack, item)
        stack.append(top)


def reverse_stack(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_bottom(stack, top)


stack = [1, 2, 3, 4, 5]
reverse_stack(stack)
print(stack)
# print(reverse_stack([1, 2, 3, 4, 5]))
# print(reverse_stack([1]))
# print(reverse_stack([]))
# print(reverse_stack([1, 5, 7, 3, 9]))
