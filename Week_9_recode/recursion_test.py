# Base case: n < 10 (any single digit non-negative number returns itself)
# How it gets smaller: n // 10 uses floor division to remove the last digit to the right on each recursio call

# def digit_sum(n: int) -> int:
#     if n < 0:
#         return None
#     if n < 10:
#         return n

#     # if n >= 10:
#     # return (n % 10) + digit_sum(n // 10)
#     # ========= OR ==========
#     last_digit = n % 10
#     remaining = n // 10
#     return last_digit + digit_sum(remaining)


# print(digit_sum(123))

# total = 0
# while n >= 10:
#     digit = n % 10
#     n = n // 10
#     total = digit + digit_sum(n)
#     return total


# print(digit_sum(12345))

# Base case: len(text) <= 1 (empty string or single character)
# How it gets smaller: text[:-1] picks from first letter to the letter before the last on each recursive call.
# OR text[1:] picks from after the first letter till the last number on each recursive call
# def reverse_text(text: str) -> str:
#     if len(text) <= 1:
#         return text
#     # last_let = text[-1]
#     # remaining = text[:-1]
#     # return last_let + reverse_text(remaining)
#     # ========== OR ==========
#     first_char = text[0]
#     remaining = text[1:]
#     return reverse_text(remaining) + first_char


# print(reverse_text("abcde"))

# Base case: text == "" (an empty string has 0 occurences)
# How it gets smaller: text[1:] picks and starts from after the first letter on each recursive call.
# def count_char(text: str, ch: str) -> int:
#     count = 0
#     if text == "":
#         return count
#     if text[0] == ch:
#         count += 1
#     remaining = text[1:]

#     return count + count_char(remaining, ch)


# print(count_char("banana", "a"))

# Base case: exp == 0 (when exp is 0 what should happen)
# How it gets smaller: (exp - 1) reduces exp until it gets to zero
def power(base: int, exp: int) -> int:
    if exp < 0:
        return None
    if exp == 0:
        return 1
    if exp >= 1:
        return base * power(base, exp - 1)

    # ========== OR ==========
    # if exp >= 1:
    #     if exp % 2 == 0:
    #         half = power(base, exp // 2)
    #         return half * half
    #     else:
    #         return base * power(base, exp - 1)


print(power(2, 10))

# def count_up(n):
#     if n == 0:
#         return
#     if n > 0:
#         count_up(n - 1)
#         print(n)
# count_up(4)

# def factorial(n):
#     if n < 0:
#         return None
#     if n <= 1:
#         return 1

#     return n * factorial(n - 1)

# print(factorial(5))
