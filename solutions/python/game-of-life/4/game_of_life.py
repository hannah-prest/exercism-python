"""Conway's game of life module"""
def tick(matrix):
    """Conway's game of life function"""
    def count_neighbors(matrix, row, col):
        offsets = [(-1,-1), (-1,0), (-1,1),
                   ( 0,-1),         ( 0,1),
                   ( 1,-1), ( 1,0), ( 1,1)]
        return sum(
            matrix[row + delta_row][col + delta_col]
            for delta_row, delta_col in offsets
            if 0 <= row + delta_row < len(matrix)
            and 0 <= col + delta_col < len(matrix[0])
        )

    
    return [
                [
                    1 if (matrix[row][col] == 1 and count_neighbors(matrix, row, col) in {2, 3})
                      or (matrix[row][col] == 0 and count_neighbors(matrix, row, col) == 3)
                    else 0
                    for col in range(len(matrix[0]))
                ]
                for row in range(len(matrix))
            ]
            