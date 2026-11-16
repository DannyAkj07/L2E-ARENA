def count_paths(rows,cols):
    if rows < 1 or cols < 1:
        return 0
    if rows == 1 or cols == 1:
        return 1

    row_path = count_paths(rows - 1, cols)
    col_path = count_paths(rows, cols - 1)

    return row_path + col_path

print(count_paths(0, 4))
print(count_paths(1, 1))
print(count_paths(3, 3))
print(count_paths(3, 2))
print(count_paths(2, 2))
print(count_paths(3, 7))
