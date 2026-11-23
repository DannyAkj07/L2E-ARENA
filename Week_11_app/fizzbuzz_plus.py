def fizzbuzz_plus(n):
    if not n:
        return []
    result = []
    for i in range(1, n + 1):
        word = ""
        if i % 3 == 0:
            word += "Fizz"
        if i % 5 == 0:
            word += "Buzz"
        if i % 7 == 0:
            word += "Bazz"
        if word == "":
            word += str(i)
        result.append(word)
    return result


print(fizzbuzz_plus(3))
print(fizzbuzz_plus(15))
print(fizzbuzz_plus(21))
print(fizzbuzz_plus(0))
# print(fizzbuzz_plus(35))
# print(fizzbuzz_plus(105))
# print(fizzbuzz_plus(4))
