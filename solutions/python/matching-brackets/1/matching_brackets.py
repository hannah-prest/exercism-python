"""Module for paired and properly nested bracket check"""
def is_paired(input_string):
    """Function for paired and properly nested bracket check"""
    brackets = []

    for c in input_string:
        if (c in {"(","{","["}):
            brackets.append(c)
        elif (c in {")","}","]"}):
            if len(brackets) == 0:
                return False
            last = brackets.pop()
        if (c == "]" and last != "[") or (c == "}" and last != "{") or (c == ")" and last != "("):
            return False
    return len(brackets) == 0