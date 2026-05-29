"""math answers"""
import string
def answer(question):
    """math answers"""
    operations = {"plus": lambda a, b: a + b, "minus": lambda a, b: a - b, "multiplied": lambda a, b: a * b, "divided": lambda a, b: a // b}
    ignored = {"what", "is", "by"}
    result = None
    operator = None
    for ele in question.lower().strip(string.punctuation).split():
        if ele.lstrip("-").isdigit():
            if result is None:
                result = int(ele)
            elif operator is None:
                raise ValueError("syntax error")
            else:
                result = operator(result, int(ele))
            operator = None
        elif ele in operations:
            if operator is not None:
                raise ValueError("syntax error")
            operator = operations[ele]
        elif ele not in ignored:
            raise ValueError("unknown operation")

    if result is None or operator is not None:
        raise ValueError("syntax error")
    
    return result