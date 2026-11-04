def max_subarray_brute(nums):
    if not nums:
        return (0, (-1, -1))
    max_sum = nums[0]
    best_start = 0
    best_end = 0

    for start in range(len(nums)):
        current_sum = 0
        for end in range(start, len(nums)):
            current_sum += nums[end]
            if current_sum > max_sum:
                max_sum = current_sum
                best_start = start
                best_end = end

    return f"sum {max_sum}, indices({best_start}, {best_end})"


def max_subarray_fast(nums):
    if not nums:
        return (0, (1, -1))
    max_sum = nums[0]
    best_start = 0
    best_end = 0
    current_start = 0
    current_sum = 0

    for i in range(len(nums)):
        if current_sum < 0:
            current_start = i
            current_sum = 0
        current_sum += nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = current_start
            best_end = i

    return (max_sum, (best_start, best_end))


print(max_subarray_fast([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray_fast([5]))
print(max_subarray_fast([-3, -1, -2]))
print(max_subarray_fast([]))

print(max_subarray_brute([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray_brute([5]))
print(max_subarray_brute([-3, -1, -2]))
print(max_subarray_brute([]))
