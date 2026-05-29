"""Conway's game of life module"""
def tick(matrix):
    """Conway's game of life function"""
    def count_neighbors(matrix, row, col):
        offsets = [(-1,-1), (-1,0), (-1,1),
                   ( 0,-1),         ( 0,1),
                   ( 1,-1), ( 1,0), ( 1,1)]
        return sum(
            matrix[row + dr][col + dc]
            for dr, dc in offsets
            if 0 <= row + dr < len(matrix)
            and 0 <= col + dc < len(matrix[0])
        )

    
    next_gen = []
    if len(matrix) >= 1: 
        rows = range(len(matrix))
        
        if len(matrix[0]) >= 1: 
            columns = range(len(matrix[0]))
        
            for row in rows:
                new_row = []
                for col in columns:
                    count_of_live_neighbors = count_neighbors(matrix, row, col)
                    is_alive = matrix[row][col] == 1
                    if (is_alive and count_of_live_neighbors in (2,3)) or (not is_alive and count_of_live_neighbors == 3):
                        new_row.append(1)
                    else:
                        new_row.append(0)
                next_gen.append(new_row)
            
    return next_gen