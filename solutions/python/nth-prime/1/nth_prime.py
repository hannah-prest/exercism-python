"""Nth Prime"""
def prime(number):
    """Nth Prime"""
    if number == 0:
        raise ValueError('there is no zeroth prime')

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False      
        return True

    counter = 0
    num = 2
    while True:
        if is_prime(num):
            counter += 1
            if counter == number:
                return num
        num += 1
        
    return None