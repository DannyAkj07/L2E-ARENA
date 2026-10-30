def mat_sum(matrix: list):
    num_row = len(matrix)
    num_col = len(matrix[0])

    for row_index, row in enumerate(matrix, 1):
        row_total = 0
        for col in row:
            row_total += col
        row_average = row_total / len(row)
        print(
            f"Row {row_index} total: {row_total} | Row {row_index} average: {row_average}")

    # for col_index in range(num_col):
    #     col_total = 0
    #     for row_index, row in enumerate(matrix):
    #         col_total += row[col_index]
    #     # col_average = col_total / num_col
    #     print(f"Column {col_index + 1} total: {col_total}")
    for col in range(num_col):
        col_total = 0
        for row in range(num_row):
            col_total += matrix[row][col]
        print(f"Column {col + 1} total: {col_total}")

mat_sum([[2, 4, 6], [1, 3, 5], [10, 20, 30]])
