def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    # saved_index = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return (mid)
            break
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return (-1)


print(binary_search([1, 3, 3, 3, 5, 8,], 1))
