"""prime factors"""
import math

def factors(value):
    """prime factors"""
    result = []

    if value > 1:     
        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False      
            return True

        primes = [n for n in range(2, int(value**0.5) + 3) if is_prime(n)]
        
        number = value
        while number > 1:
            for prime_num in primes:
                if number % prime_num == 0:
                    result.append(prime_num)
                    number = number // prime_num
                    break
            else:  
                result.append(number)
                break
    return result