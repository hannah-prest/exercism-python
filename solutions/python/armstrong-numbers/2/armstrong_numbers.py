"""Module for determining if a number is an Armstrong Number"""
def is_armstrong_number(number):
    """Function for determining if a number is an Armstrong Number"""
    counts_of_digits = len(str(number))
    digits = [int(digit) for digit in str(number)]
    sum_of_digits_to_the_power_of_count_of_digits = 0
    for digit in digits:
        sum_of_digits_to_the_power_of_count_of_digits += digit ** counts_of_digits
    return sum_of_digits_to_the_power_of_count_of_digits == number
