"""Module for paired and properly nested bracket check"""
def is_paired(input_string):
    """Function for paired and properly nested bracket check"""
    brackets = []
    matching = {")": "(", "}": "{", "]": "["}

    for char in input_string:
        if char in {"(","{","["}:
            brackets.append(char)
        elif char in matching:
            if not brackets or brackets.pop() != matching[char]:
                return False
    return len(brackets) == 0