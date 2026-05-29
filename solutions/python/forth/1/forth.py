"""Forth subset evaluator"""
import math

# subclassing the Exception to create a StackUnderflowError
class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message

def is_digit_or_neg(s):
    if not s:
        return False
    if s.startswith('-'):
        return s[1:].isdigit()
    return s.isdigit()

def evaluate(input_data):
    """Forth subset evaluator"""

    operations = {"+": lambda x, y: x+y,
                          "-": lambda x, y: x-y,
                          "*": lambda x, y: x*y,
                          "/": lambda x, y: x//y,
                          "dup": lambda x, y: [x, y, y] if x is not None else [y,y],
                          "drop": lambda x, y: [x] if x is not None else [],
                          "swap": lambda x, y: [y,x],
                          "over": lambda x, y: [x, y, x]
                         }
    translations = {}

    result = []
    main_op = input_data[-1].lower()
    if len(input_data) > 1:  
        for operation in input_data[:-1]:
            redefine= operation.lower().replace(":","").replace(";","").strip().split()
            key = redefine[0]
            if is_digit_or_neg(key):
                raise ValueError("illegal operation")
            translations.setdefault(key, "")
            translation = " ".join(redefine[1:])
            for old, new in translations.items():
                translation = translation.replace(old, new)
            translations[key] = translation
    
    for old, new in translations.items():
            main_op = main_op.replace(old, new)

    if main_op.startswith(":"):
        raise ValueError("illegal operation")
        
    split = main_op.split()
    valid_nondigits = {"+","-","*","/","dup","drop","swap","over","dup-twice"}
    valid_for_single_digit = {"dup","drop","dup-twice"}
    invalid_count = sum(1 for item in split if item not in valid_nondigits and not is_digit_or_neg(item))
    if invalid_count > 0:
        raise ValueError("undefined operation")
    numbers = [int(item) for item in split if item not in valid_nondigits and is_digit_or_neg(item)]
    number_count = len(numbers)
    valid_nondigits_count = sum(1 for item in split if item in valid_nondigits)
    if valid_nondigits_count > 0 and number_count < 2 and not (number_count >= 1 and split[-1] in valid_for_single_digit):
        raise StackUnderflowError("Insufficient number of items in stack")

    for item in split:
        if item in valid_nondigits:
            last = result.pop()
            first = None
            if len(result) > 0:
                first = result.pop()
            if item == "/" and last == 0:
                raise ZeroDivisionError("divide by zero")
            op_res = operations[item](first, last)       
            if isinstance(op_res, list):
                result.extend(op_res)
            else:
                result.append(op_res)
        else:
            result.append(int(item))
        
    return result