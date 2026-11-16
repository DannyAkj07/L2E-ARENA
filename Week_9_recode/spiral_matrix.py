def spiral_order(matrix):
    if not matrix:
        return []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    result = []
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiral_order([[1, 2, 3, 4], [5, 6, 7, 8]]))
print(spiral_order([[1], [2], [3]]))
print(spiral_order([]))

# ======= BONUS ======
def spiral_fill(n: int) -> list[list[int]]:
    if n <= 0:
        return []

    # 1. Build an n x n grid filled with 0s (using standard loops, no list comprehensions)
    grid = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append(0)
        grid.append(row)

    # 2. Initialize the four shrinking fences and our counter
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    num = 1

    # 3. Walk the exact same spiral path, writing 'num' into each slot
    while top <= bottom and left <= right:
        # Top row (left -> right)
        for col in range(left, right + 1):
            grid[top][col] = num
            num += 1
        top += 1

        # Right column (top -> bottom)
        for row in range(top, bottom + 1):
            grid[row][right] = num
            num += 1
        right -= 1

        # Bottom row (right -> left)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                grid[bottom][col] = num
                num += 1
            bottom -= 1

        # Left column (bottom -> top)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                grid[row][left] = num
                num += 1
            left += 1

    return grid


print(spiral_fill(2))  # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
