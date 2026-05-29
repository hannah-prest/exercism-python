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
    all_ops = binary_ops.keys() | unary_ops.keys()
    
    invalid = [item for item in split if item not in all_ops and not is_digit_or_neg(item)]
    if invalid:
        raise ValueError("undefined operation")

    result = []
    for item in split:
        if item in binary_ops:
            if len(result) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            if item == "/" and result[-1] == 0:
                raise ZeroDivisionError("divide by zero")
            y, x = result.pop(), result.pop()
            op_result = binary_ops[item](x, y)
            result.append(op_result)
        elif item in unary_ops:
            if len(result) < 1:
                raise StackUnderflowError("Insufficient number of items in stack")
            if item in ("swap", "over"):
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                y, x = result.pop(), result.pop()
                result.extend(unary_ops[item](x, y))
            else:
                x = result.pop()
                result.extend(unary_ops[item](x))
        else:
            result.append(int(item))

    return result