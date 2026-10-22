# def sum_list(nums: list[int]) -> int:
#     add = 0
#     for item in nums:
#         add += item
#     return add


# print(sum_list([1, 2, 3, 4, 5]))

def sum_list(nums: list[int]) -> int:
    add = 0
    for item in range(len(nums)):
        add += nums[item]
        # print(item)
    return add


print(sum_list([1, 2, 6, 4]))

