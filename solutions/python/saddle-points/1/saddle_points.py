"""saddle points"""
def saddle_points(matrix):
    """saddle points"""
    height = len(matrix)
    width = 0 if height == 0 else len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("irregular matrix")

    def check_cell(field, row_i, col_i):
        cell = field[row_i][col_i]
        col = [row[col_i] for row in field]
        row = field[row_i]
        return cell == min(col) and cell == max(row)

    return [
        {"row": row + 1, "column": col + 1}
        for col in range(width)
        for row in range(height)
        if check_cell(matrix, row, col)
    ]