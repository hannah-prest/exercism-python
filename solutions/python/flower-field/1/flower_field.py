"""Flower Field"""
def annotate(garden):
    """Flower Field"""
    width = 0 if len(garden) == 0 else len(garden[0])
    valid_chars = {"*", " "}
    if any(len(row) != width for row in garden) or any(set(row) - valid_chars for row in garden):
        raise ValueError("The board is invalid with current input.")
    
    def count_neighbors(matrix, row, col):
        offsets = [(-1,-1), (-1,0), (-1,1),
                   ( 0,-1),         ( 0,1),
                   ( 1,-1), ( 1,0), ( 1,1)]
        return sum(
            matrix[row + dr][col + dc] == "*"
            for dr, dc in offsets
            if 0 <= row + dr < len(matrix)
            and 0 <= col + dc < len(matrix[0])
        )

    def cell(row, col):
        if garden[row][col] == "*":
            return "*"
        count = count_neighbors(garden, row, col)
        return str(count) if count > 0 else " "

    return [
        "".join(cell(row, col) for col in range(width))
        for row in range(len(garden))
    ]