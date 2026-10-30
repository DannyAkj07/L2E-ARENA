def convert_temperature(temp: float, target_unit: str) -> float:
    if target_unit == "C":
        return round((temp * 9/5) + 32,2)
    if target_unit == "F":
        return round((temp - 32) * 5/9,2)


print(convert_temperature(100.0, "F"))
