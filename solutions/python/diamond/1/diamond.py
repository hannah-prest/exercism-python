"""diamond kata"""
import string
def rows(letter):
    """diamond kata"""
    middle_rows = string.ascii_uppercase.index(letter)
    string_len_goal = 1+(middle_rows*2)
    center = string_len_goal // 2
    result = []
    for index in range(middle_rows+1):
        new_line = [" " for i in  range(string_len_goal)]
        new_line[center - index] = string.ascii_uppercase[index]
        if center + index < len(new_line):
            new_line[center + index] = string.ascii_uppercase[index]
        result.append("".join(new_line))
    for index in reversed(range(middle_rows)):
        new_line = [" " for i in  range(string_len_goal)]
        new_line[center - index] = string.ascii_uppercase[index]
        if center + index < len(new_line):
            new_line[center + index] = string.ascii_uppercase[index]
        result.append("".join(new_line))
    return result