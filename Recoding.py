# def sum_list(nums: list[int]) -> int:
#     add = 0
#     for item in nums:
#         add += item
#     return add


# print(sum_list([1, 2, 3, 4, 5]))

# def sum_list(nums: list[int]) -> int:
#     add = 0
#     for item in range(len(nums)):
#         add += nums[item]
#         print(item)
#     return add


# print(sum_list([1, 2, 6, 4]))

def find_min_max(nums: list[int]) -> tuple[int,int]:
    smallest = nums[0]
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return(largest,smallest)

print(find_min_max([-10, 0, 50, -3])) 