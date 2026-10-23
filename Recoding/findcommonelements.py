def find_common_elements(list1: list, list2: list) -> list:
    new_list = []
    for x in list1:
        for y in list2:
            if y == x and y not in new_list:
                new_list.append(y)
    # for item in list1:
    #     if item in list2 and item not in new_list:
    #             new_list.append(item)
    return new_list


print(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6, 3]))
print(find_common_elements(["a", "b", "c"], ["x", "a", "y", "z"]))
