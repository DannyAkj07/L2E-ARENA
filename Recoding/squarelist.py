def square(num: int) -> int:
    return num ** 2


def square_elements(nums: list[int]) -> list[int]:
    num_square = [num ** 2 for num in nums]
    return num_square
    return list(map(lambda x: x ** 2, nums))
    # return list(map(square, nums))


print(square_elements([1, 2, 3, 4]))
print(square_elements([-2, 0, 5]))
