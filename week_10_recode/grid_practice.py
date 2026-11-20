def count_paths(rows, cols):
    if rows < 1 or cols < 1:
        return 0
    if rows == 1 or cols == 1:
        return 1

    rows_down = count_paths(rows - 1, cols)
    cols_down = count_paths(rows, cols - 1)

    return rows_down + cols_down


print(count_paths(2, 2))
print(count_paths(1, 0))
print(count_paths(3, 2))
print(count_paths(4, 3))
print(count_paths(3, 7))
