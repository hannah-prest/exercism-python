"""egg count"""
def egg_count(display_value):
    """egg count"""         
    result = []
    while display_value > 0:
        result.append(display_value % 2)
        display_value = display_value // 2         
    return  sum(result)