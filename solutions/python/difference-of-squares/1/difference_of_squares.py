"""difference of squares"""
def square_of_sum(number):
    """square of sum"""
    return sum(range(1,number+1))**2


def sum_of_squares(number):
    """sum of squares"""
    return sum(i**2 for i in range(1,number+1))


def difference_of_squares(number):
    """difference of squares"""
    return square_of_sum(number) - sum_of_squares(number)
