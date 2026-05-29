"""Module to rebase numbers"""
def rebase(input_base, digits, output_base):
    """Function to rebase numbers"""
    
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    base10 = sum (
        digit * (input_base**power)
        for digit, power in zip(digits, reversed(range(len(digits))))
    )

    if len(digits) == 0 or base10 == 0:
        return [0]
    
    result = []
    while base10 > 0:
        result.append(base10 % output_base)
        base10 = base10 // output_base
    
    return  result[::-1]
