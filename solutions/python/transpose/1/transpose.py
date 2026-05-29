"""transpose"""
from itertools import zip_longest
def transpose(text):
    """transpose"""
    rows = text.split("\n")
    result = []
    for chars in zip_longest(*rows):  
        last = max(i for i, c in enumerate(chars) if c is not None)
        row = "".join(c if c is not None else " " for c in chars[:last+1])
        result.append(row)
    return "\n".join(result)
