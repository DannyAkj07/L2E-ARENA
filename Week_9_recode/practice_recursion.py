# def count_down(n):
#     while n > 0:
#         print(n)
#         n = n - 1
#     print("BLAST OFF")

# count_down(5)

# def countdown_recursion(n):
#     if n == 0:
#         print("BLAST OFF!")
#         return
#     print(n)

#     countdown_recursion(n - 1)

# countdown_recursion(5)

# def count_up(n):
#     if n == 0:
#         return
#     count_up(n - 1)
#     print(n)


# count_up(3)

def factorial(n):
    if n < 0:
        return None
    if n <= 1:
        return 1
    if n > 1:        
        return n * factorial(n - 1)

print(factorial(4))

