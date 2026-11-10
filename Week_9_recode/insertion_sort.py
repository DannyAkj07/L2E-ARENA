def insertion_sort(nums):
    comparison = 0
    shift = 0

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0:
            comparison += 1
            if nums[j] > key:
                nums[j + 1] = nums[j]
                shift += 1
                j -= 1
            else:
                break
            
        nums[j + 1] = key

    return (comparison, shift)


print(insertion_sort([5, 2, 4, 1]))
