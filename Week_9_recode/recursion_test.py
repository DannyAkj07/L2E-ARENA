def digit_sum(n: int) -> int:

    if n < 10:
        return n
    
    total = 0
    while n >= 10:
        digit = n % 10
        n = n // 10
        total = digit + digit_sum(n)
        return total


print(digit_sum(12345))


def reverse_text(text: str) -> str:
    pass


def count_char(text: str, ch: str) -> int:
    pass


def power(base: int, exp: int) -> int:
    pass
