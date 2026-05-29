"""Module for wheat and chessboard problem."""

def square(number):
    """the number of grains on a given square"""
    if (number < 1 or number > 64):
        # when the square value is not in the acceptable range        
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)


def total():
    """the total number of grains on the chessboard"""
    squares_sum = 0
    for i in range(1, 65): # pylint: disable=invalid-name
        squares_sum += square(i) # pylint: disable=invalid-name
    return squares_sum
