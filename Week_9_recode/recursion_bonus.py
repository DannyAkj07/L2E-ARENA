def power(base: int, exp: int) -> int:
    if exp < 0:
        return None
    if exp == 0:
        return 1
    if exp >= 1:
        if exp % 2 == 0:
            half = power(base, exp // 2)
            return half * half
        else:
            return base * power(base, exp - 1)


print(power(2, 10))