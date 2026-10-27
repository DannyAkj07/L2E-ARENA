def two_sum(nums: list[int], target: int) -> list[int]:
    # for index1, i in enumerate(nums):
    #     for index2, j in enumerate(nums):
    #         if index1 == index2:
    #             continue
    #         if i + j == target:
    #             return [index1, index2]

    # ========== OR ==========

    seen = {}
    for index, i in enumerate(nums):
        combined = target - i
        if combined in seen:
            return [seen[combined], index]
        seen[i] = index 

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
