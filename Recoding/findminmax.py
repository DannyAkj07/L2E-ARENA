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