"""spiral matrix"""

RIGHT = "right"
LEFT = "left"
UP = "up"
DOWN = "down"   

DIRECTIONS = {
    RIGHT: (0, 1, DOWN),
    DOWN:  (1, 0, LEFT),
    LEFT:  (0, -1, UP),
    UP:    (-1, 0, RIGHT),
}

def spiral_matrix(size):
    """spiral matrix"""
    matrix = [[None] * size for _ in range(size)]
    row, col = 0, 0
    direction = RIGHT

    for number in range(1, size**2+1):
        matrix[row][col] = number
        dr, dc, next_direction = DIRECTIONS[direction]
        next_row, next_col = row + dr, col + dc
        if not (0 <= next_row < size and 0 <= next_col < size and matrix[next_row][next_col] is None):
            direction = next_direction
            dr, dc, _ = DIRECTIONS[direction]
        row += dr
        col += dc    

    return matrix   
