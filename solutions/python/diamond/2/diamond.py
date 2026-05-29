"""diamond kata"""
import string
def rows(letter):
    """diamond kata"""
    def make_row(index, center, width):
        row = [" "] * width
        row[center - index] = string.ascii_uppercase[index]
        if index != 0:
            row[center + index] = string.ascii_uppercase[index]
        return "".join(row)
    
    middle_rows = string.ascii_uppercase.index(letter)
    string_len_goal = 1+(middle_rows*2)
    center = string_len_goal // 2
    indices = list(range(middle_rows + 1))
    return [make_row(index, center, string_len_goal) for index in indices + indices[-2::-1]]