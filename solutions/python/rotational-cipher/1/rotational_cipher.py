"""Module rotational cipher"""
import string
def rotate(text, key):
    """Function rotational cipher"""
    plain_lower = string.ascii_lowercase
    plain_upper = string.ascii_uppercase
    shifted_lower = plain_lower[key:] + plain_lower[:key]
    shifted_upper = plain_upper[key:] + plain_upper[:key]
    table = str.maketrans(plain_lower + plain_upper, shifted_lower + shifted_upper)

    return text.translate(table)