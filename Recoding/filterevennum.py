def filter_even_numbers(nums: list[int]) -> list[int]:
    new_nums = [num for num in nums if num % 2 == 0]
    return new_nums


print(filter_even_numbers([1, 2, 3, 4, 5, 6]))
