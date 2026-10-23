def remove_duplicates(nums: list) -> list:
    if not nums:
        return []
    new_list = []
    for i in nums:
        if i not in new_list:
            new_list.append(i)
    return new_list

    # ==== OR ====

    # return list(dict.fromkeys(nums))

print(remove_duplicates(["apple", "banana", "apple", "cherry"]))
print(remove_duplicates([1, 2, 2, 3, 4, 3, 5]))