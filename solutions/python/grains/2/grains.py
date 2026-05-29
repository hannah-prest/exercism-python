def square(number):
    if (number < 1 or number > 64):
        # when the square value is not in the acceptable range        
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)


def total():
    squares_sum = 0
    for i in range(1, 65):
        squares_sum += square(i)
    return squares_sum
