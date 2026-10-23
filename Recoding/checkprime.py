def is_prime(n: int) -> bool:
    if n <= 1:
        return "Not a valid integer"
    for i in range(2, n):
        if n % i == 0:
            return False        
    return True


print(is_prime(15))
