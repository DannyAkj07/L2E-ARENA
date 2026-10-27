# def sum_nested_list(nested_list: list) -> int:
#     new_list = []
#     for item in nested_list:
#         if isinstance(item, list):
#             new_list.append(sum_nested_list(item))
#         else:
#             new_list.append(item)

#     sum_list = 0
#     for num in new_list:
#         sum_list += num
#     return sum_list


def sum_nested_list(nested_list: list) -> int:
    sum_list = 0
    for item in nested_list:
        if isinstance(item,list):
            sum_list += sum_nested_list(item)
        else:
            sum_list += item
    return sum_list


print(sum_nested_list([[1,[2,3], 1], 2, [1, 1]]))
print(sum_nested_list([1, [2, 3], [4, [5]]]))
