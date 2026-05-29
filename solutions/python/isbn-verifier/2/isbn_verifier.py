"""ISBN module"""
def is_valid(isbn):
    """ISBN function"""
    valid_characters = ('X','x','0','1','2','3','4','5','6','7','8','9','-')
    if not all(unit in valid_characters for unit in isbn):
        return False
    if any(unit == 'X' for unit in isbn) and not isbn[-1] == 'X':
        return False
    
    scrubbed_isbn = isbn.replace('-','')

    if len(scrubbed_isbn) != 10:
        return False
    
    running_total = 0
    countdown = 10
    for iterator in range(10):
        digit = scrubbed_isbn[iterator]
        if digit in {'X','x'}:
            digit = 10
        running_total += int(digit) * countdown
        countdown -= 1
    return running_total % 11 == 0
        
