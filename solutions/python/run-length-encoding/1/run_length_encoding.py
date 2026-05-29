"""rle"""
def decode(string):
    """decode"""
    result = ""
    index = 0
    while index < len(string):
        char = string[index]
        num = ""
        while char.isdigit():
            num += char
            index += 1
            char = string[index]
        count = int(num) if num else 1
        result += char * count
        index += 1
        
    return result


def encode(string):
    """encode"""
    if not string:
        return ""
    result = ""
    curr_char = string[0]
    curr_count = 1
    for char in string[1:]:
        if char == curr_char:
            curr_count += 1
        else:
            result += f"{curr_count if curr_count > 1 else ""}{curr_char}"
            curr_char = char
            curr_count = 1
    result += f"{curr_count if curr_count > 1 else ""}{curr_char}"
    return result