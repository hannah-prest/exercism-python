"""Module to classify numbers"""
import math
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        # if a number to be classified is less than 1.
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = 0

    if number > 1:
        factors_except_self = {1}
        for iterator in range(2,int(math.sqrt(number))+1):
            if number % iterator == 0:
                factors_except_self.add(iterator)
                factors_except_self.add(number // iterator)
        aliquot_sum = sum(factors_except_self)

    if aliquot_sum == number:
        return "perfect"
    if number < aliquot_sum:
        return "abundant"
    return "deficient"