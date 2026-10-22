def even_odd(n: int) -> bool:
    if not n:
        return "Not an integer"
    if n % 2 == 0:
        return True
    else:
        return False


print(even_odd(7))
