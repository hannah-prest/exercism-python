"""squareroot of positive integers"""
def square_root(number):
    """squareroot of positive integers"""
    low = 1
    high = number
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            low = mid + 1
        else:
            high = mid - 1         
    return low
