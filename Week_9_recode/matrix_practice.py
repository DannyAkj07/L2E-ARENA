
# grid = [
#     [10, 20, 30],   # Row 0
#     [40, 50, 60],   # Row 1
#     [70, 80, 90]    # Row 2
# ]
# # for i in range(3, -1, -1):
# #     print(i)

# top = 0
# bottom = len(grid) - 1
# left = 0
# right = len(grid[0]) - 1

# for col in range(left, right + 1):
#     print(grid[top][col])

# for row in range(top, bottom + 1):
#     print(grid[row][right])

def matrix(grid):
    top = 0
    bottom = len(grid) - 1
    left = 0
    right = len(grid[0]) - 1

    for col in range(right, left - 1, -1):
        print(grid[bottom][col])

    for row in range(bottom, top - 1, -1):
        print(grid[row][left])


def outer_ring(grid):
    top = 0
    bottom = len(grid) - 1
    left = 0
    right = len(grid[0]) - 1

    result = []
    for col in range(left, right + 1):
        result.append(grid[top][col])
    top += 1
    for row in range(top, bottom + 1):
        result.append(grid[row][right])
    right -= 1
    for col in range(right, left - 1, -1):
        result.append(grid[bottom][col])
    bottom -= 1
    for row in range(bottom, top - 1, -1):
        result.append(grid[row][left])
    left += 1
    return result


print(outer_ring([[10, 20, 30], [40, 50, 60], [70, 80, 90]]))
# print(2 << 3)

# matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
