# def filter_even_numbers(nums: list[int]) -> list[int]:
#     # new_nums = [num for num in nums if num % 2 == 0]
#     new_nums = list(filter(lambda x: x % 2 == 0, nums))
#     return new_nums
def is_even(num: int) -> bool:
    return num % 2 == 0


def filter_even_numbers(nums: list[int]) -> list[int]:
    return list(filter(is_even, nums))


print(filter_even_numbers([1, 2, 3, 4, 5, 6]))
print(filter_even_numbers([1, 3, 5, 7]))
