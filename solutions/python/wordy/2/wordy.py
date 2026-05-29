"""math answers"""
import string
def answer(question):
    """math answers"""
    operations = {"plus": lambda a, b: a + b, "minus": lambda a, b: a - b, "multiplied": lambda a, b: a * b, "divided": lambda a, b: a // b}
    ignored = {"what", "is", "by"}
    result = None
    op = None
    for ele in question.lower().strip(string.punctuation).split():
        if ele.lstrip("-").isdigit():
            if result is None:
                result = int(ele)
            elif op is None:
                raise ValueError("syntax error")
            else:
                result = op(result, int(ele))
            op = None
        elif ele in operations:
            if op is not None:
                raise ValueError("syntax error")
            op = operations[ele]
        elif ele not in ignored:
            raise ValueError("unknown operation")

    if result is None or op is not None:
        raise ValueError("syntax error")
    
    return result