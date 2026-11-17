def insert_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    else:
        top = stack.pop()
        insert_bottom(stack, item)
        stack.append(top)
    return stack

print(insert_bottom([2, 3, 4], 1))

def reverse_stack(stack):
    if not stack:
        return stack
    else:
        top = stack.pop()

        reverse_stack(stack)
        insert_bottom(stack, top)
    return stack


print(reverse_stack([2, 3, 4]))
print(reverse_stack([1, 2, 3, 4, 5]))

