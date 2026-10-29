def list_anayser(nums: list):
    if not nums:
        print("Invalid entry")
        return
    smallest = nums[0]
    largest = nums[0]
    total = 0
    index_small = 0
    index_large = 0
    
    for index, num in enumerate(nums):
        if num < smallest:
            smallest = num
            index_small = index
        if num > largest:
            largest = num
            index_large = index
        total += num
    average = total / len(nums)
    above_average = 0
    for num in nums:
        if num > average:
            above_average += 1
    # print(f"Smallest: {smallest} (at index {index_small})\nLargest: {largest} (at index {index_large})\nTotal: {total}\nAverage: {average:.2f}\nNumbers above average: {above_average}")

    # ======== OR ======
#     print(f"""
# Smallest: {smallest} (at index {index_small})
# Largest: {largest} (at index {index_large})
# Total: {total}
# Average: {average:.2f}
# Numbers above average: {above_average}
# """)
    # ======= OR =======
    print(f"Smallest: {smallest} (at index {index_small})")
    print(f"Largest: {largest} (at index {index_large})")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Numbers above average: {above_average}")
    


list_anayser([12, 5, 27, 8, 14, 27, 3])
list_anayser([])
