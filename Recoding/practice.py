def sum_nested_list(nested_list: list) -> int:
    if not nested_list:
        return []
    
    total = 0
    for item in nested_list:
        if isinstance(item,list):
            total += sum_nested_list(item)
        else:
            total += item
    return total

print(sum_nested_list([1, [2, 3], [4, [5]]]))