"""Forth subset evaluator"""

class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message

def is_digit_or_neg(s):
    try:
        int(s)
        return True
    except (ValueError, TypeError):
        return False

def evaluate(input_data):
    """Forth subset evaluator"""
    binary_ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x // y,
    }
    unary_ops = {
        "dup": lambda x: [x, x],
        "drop": lambda x: [],
    }
    binary_list_return_ops = {
        "swap": lambda x, y: [y, x],
        "over": lambda x, y: [x, y, x],
    }
    
    translations = {}
    main_op = input_data[-1].lower()
    
    for operation in input_data[:-1]:
        redefine = operation.lower().replace(":", "").replace(";", "").strip().split()
        key = redefine[0]
        if is_digit_or_neg(key):
            raise ValueError("illegal operation")
        translation = " ".join(redefine[1:])
        for old, new in translations.items():
            translation = translation.replace(old, new)
        translations[key] = translation

    for old, new in translations.items():
        main_op = main_op.replace(old, new)

    if main_op.startswith(":"):
        raise ValueError("illegal operation")

    split = main_op.split()
    all_ops = binary_ops.keys() | unary_ops.keys() | binary_list_return_ops.keys()
    
    invalid = [item for item in split if item not in all_ops and not is_digit_or_neg(item)]
    if invalid:
        raise ValueError("undefined operation")

    def apply_op(item, result, ops, pop_count):
        if len(result) < pop_count:
            raise StackUnderflowError("Insufficient number of items in stack")
        y = result.pop()
        if item == "/" and y == 0:
            raise ZeroDivisionError("divide by zero")
            
        if pop_count > 1:
            x = result.pop()      
            res = ops[item](x, y)
            if isinstance(res, list):
                result.extend(res)  
            else: 
                result.append(res)
        else:
            result.extend(ops[item](y))

    result = []
    for item in split:
        if item in binary_ops:
            apply_op(item, result, binary_ops, 2)
        elif item in unary_ops:
            apply_op(item, result, unary_ops, 1)
        elif item in binary_list_return_ops:
            apply_op(item, result, binary_list_return_ops, 2)
        else:
            result.append(int(item))

    return result