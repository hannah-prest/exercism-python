"""Module for the collatz conjecture"""
def steps(number):
    """Function for the collatz conjecture"""
    if number <=0:
        # example when argument is zero or a negative integer
        raise ValueError("Only positive integers are allowed")

    if number == 1:
        return 0

    if number % 2 == 0:
        bubble_up = steps(number / 2)
        return bubble_up + 1
        
    bubble_up = steps((number * 3)+1)
    return bubble_up + 1
