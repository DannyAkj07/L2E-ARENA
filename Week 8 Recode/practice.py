def binary_search(nums, target) -> tuple[int, int]:
    lowest = 0
    highest = len(nums) - 1

    saved_index = -1
    comparison = 0

    while lowest <= highest:
        comparison += 1
        mid_point = (lowest + highest) // 2
        if nums[mid_point] == target:
            saved_index = mid_point
            highest = mid_point - 1
        else:
            if nums[mid_point] > target:
                highest = mid_point - 1
            else:
                lowest = mid_point + 1

    return (saved_index, comparison)


print(binary_search([1, 3, 3, 3, 5, 8], 3))
print(binary_search([1, 3, 5, 8], 4))
print(binary_search([],7))
