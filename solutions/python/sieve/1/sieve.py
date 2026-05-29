"""primes under limit"""
def primes(limit):
    """primes under limit"""
    
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for index in range(2, int(limit**0.5) + 1):
        if sieve[index]:
            for sub_index in range(index*index, limit + 1, index):
                sieve[sub_index] = False
    return [index for index in range(2, limit + 1) if sieve[index]]