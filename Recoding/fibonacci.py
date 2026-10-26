def fibonacci(n:int) -> list:
    if n == 0:
        return []
    if n == 1:
        return [0]

    res = [0,1]
    for i in range(n):
        if len(res) == n:
            return res
        res.append(res[i] + res[i + 1])

print(fibonacci(5))
