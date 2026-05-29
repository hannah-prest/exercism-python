"""largest product"""
import math
def series_product_generator(input, size):
    """yields the next product in the series"""
    for i in range(len(input) - size + 1):
        yield math.prod(int(d) for d in input[i:i+size])

def largest_product(series, size):
    """largest product"""
    if size > len(series):
        raise ValueError("span must not exceed string length")
    
    if size < 0:
        raise ValueError("span must not be negative")
    
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    
    return max(series_product_generator(series, size), default=0)