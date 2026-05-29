"""Nth Prime"""
def prime_generator():
    """yields primes"""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

def is_prime(num):
    """returns if number is prime"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False      
    return True

def prime(number):
    """Nth Prime"""
    if number == 0:
        raise ValueError('there is no zeroth prime')

    prime_gen = prime_generator()
    for _ in range(number - 1):
        next(prime_gen)
    return next(prime_gen)