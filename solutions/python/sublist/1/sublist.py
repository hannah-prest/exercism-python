"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = -1
SUPERLIST = 1
EQUAL = 0
UNEQUAL = None


def sublist(list_one, list_two):
    """Function for determining sublist type"""
    def is_sublist(smaller, larger):
        if not smaller:
            return True
        small_len = len(smaller)
        max_start_for_valid_sublist = len(larger) - small_len + 1
        return any(larger[index:index+small_len] == smaller for index in range(max_start_for_valid_sublist))
    
    if list_one == list_two:
        return EQUAL
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL