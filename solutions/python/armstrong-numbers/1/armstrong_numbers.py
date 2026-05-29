"""Module for determining if a number is an Armstrong Number"""
def is_armstrong_number(number):
    """Function for determining if a number is an Armstrong Number"""
    counts_of_digits = len(str(number))
    digits = [int(d) for d in str(number)]
    sum = 0
    for digit in digits:
        sum += digit ** counts_of_digits
    return sum == number
