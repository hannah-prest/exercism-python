"""Module for paired and properly nested bracket check"""
def is_paired(input_string):
    """Function for paired and properly nested bracket check"""
    brackets = []

    for char in input_string:
        if (char in {"(","{","["}):
            brackets.append(char)
        elif (char in {")","}","]"}):
            if len(brackets) == 0:
                return False
            last = brackets.pop()
            if (char == "]" and last != "[") or (char == "}" and last != "{") or (char == ")" and last != "("):
                return False
    return len(brackets) == 0