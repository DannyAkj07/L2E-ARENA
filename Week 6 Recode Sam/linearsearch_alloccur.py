def linear_search(nums: list, target: int):
    indices = []
    # count = len(indices)
    # if target not in nums:
    #     print("Target not found")
    #     return
    for index, num in enumerate(nums):
        if num == target:
            indices.append(index)

    if not indices:
        print("Target not found")
        return
    
    count = len(indices)
    first = indices[0]
    last = indices[-1]
    print(
        f"Found at indices: {indices} | Count: {count} | First: {first} | Last: {last}")


linear_search([14, 7, 22, 9, 7, 31, 7, 5], 7)
