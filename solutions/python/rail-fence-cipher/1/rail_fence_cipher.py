"""rail fence cipher"""
import math
STAR = "*"

def encode(message, rails):
    """encode"""
    cipher = [["" for _ in range(len(message))] for _ in range(rails)]
    rows = zigzag_indexes(rails)
    for col, char in enumerate(message):
        row = rows[col % len(rows)]
        cipher[row][col] = char
    return "".join(char for row in cipher for char in row)

def decode(encoded_message, rails):
    """decode"""
    matrix = get_zigzag_matrix(rails,len(encoded_message))
    message_index = 0
    for row_index in range(rails):
        for col_index in range(len(encoded_message)):
            if ((matrix[row_index][col_index] == STAR) and
            (message_index < len(encoded_message))):
                matrix[row_index][col_index] = encoded_message[message_index]
                message_index += 1
    transposed = [list(row) for row in zip(*matrix)]
    return "".join(char for row in transposed for char in row)
    
def get_zigzag_matrix(height, width):
    """returns a matrix with a zigzag of the value of STAR"""
    matrix = [["" for _ in range(width)] for _ in range(height)]
    rows = zigzag_indexes(height)
    for col in range(width):
        row = rows[col % len(rows)]
        matrix[row][col] = STAR
    return matrix

def zigzag_indexes(height):
    """get row indexes of the zigzag"""
    if height < 0:
        return []
    return list(range(0, height)) + list(range(height - 2, 0, -1))