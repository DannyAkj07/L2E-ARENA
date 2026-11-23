def stats(nums):
    if not nums:
        return None
    smallest = nums[0]
    largest = nums[0]
    count = 0
    for i in nums:
        count += i
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    average = round(count/len(nums),2)
    return (smallest, largest, average)

print(stats([4, 9, 2, 7]))
print(stats([5]))
print(stats([-3, -1, -2]))
print(stats([]))
print(stats([1.5, 2.5, 3.0]))
print(stats([-10, 0, 10]))
