def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    # return n * factorial(n - 1)
    # ====== OR ======
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


print(factorial(1))
