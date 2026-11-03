# def binary_search(nums, target) -> tuple[int, int]:
#     lowest = 0
#     highest = len(nums) - 1

#     saved_index = -1
#     comparison = 0

#     while lowest <= highest:
#         comparison += 1
#         mid_point = (lowest + highest) // 2
#         if nums[mid_point] == target:
#             saved_index = mid_point
#             highest = mid_point - 1
#         else:
#             if nums[mid_point] > target:
#                 highest = mid_point - 1
#             else:
#                 lowest = mid_point + 1

#     return (saved_index, comparison)


# print(binary_search([1, 3, 3, 3, 5, 8], 3))
# print(binary_search([1, 3, 5, 8], 4))
# print(binary_search([],7))

def sub_array(nums):
    if not nums:
        return (0,(-1,-1))
    
    max_sum = nums[0]
    best_start = 0
    best_end = 0

    for start in range(len(nums)):
        current_sum = 0
        for end in range(start,len(nums)):
            current_sum += nums[end]
            if current_sum > max_sum:
                max_sum = current_sum
                best_start = start
                best_end = end
    return f"Sum {max_sum}, indices ({best_start},{best_end})"

print(sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(sub_array([5]))
print(sub_array([-3, -1, -2]))
print(sub_array([]))

