def safe_divide(a: float, b: float) -> float | str:
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"


print(safe_divide(5, 0))
