def convert_temperature(temp: float, target_unit: str) -> float:
    if target_unit == "C":
        return (temp * 9/5) + 32
    if target_unit == "F":
        return (temp - 32) * 5/9
    
print(convert_temperature(100.0, "F"))