def can_sum(nums, target, i = 0):
    if target == 0:
        return True
    if i == len(nums):
        return False
    return can_sum(nums, target, i + 1) or can_sum(nums, target - nums[i], i + 1)

print(can_sum([2,4,6,10], 16))
print(can_sum([3,5,7], 12))
print(can_sum([-3,4,5], 3))