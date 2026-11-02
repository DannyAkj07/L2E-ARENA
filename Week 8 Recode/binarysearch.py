def binary_search(nums, target) -> tuple[int, int]:
    low_point = 0
    high_point = len(nums) - 1

    comparison = 0
    saved_index = -1
    while low_point <= high_point:
        comparison += 1
        mid = (low_point + high_point) // 2
        # comparison += 1
        if nums[mid] == target:
            saved_index = mid
            high_point = mid - 1

        else:
            # comparison += 1
            if nums[mid] < target:
                low_point = mid + 1
            else:
                high_point = mid - 1

    return (saved_index, comparison)


print(binary_search([1, 3, 3, 3, 5, 8], 3))
print(binary_search([1, 3, 5, 8], 4))
print(binary_search([], 7))
