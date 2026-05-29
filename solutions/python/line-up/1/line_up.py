"""Line UP"""
def line_up(name, number):
    """Line UP"""
    str_number = str(number)
    suffix = "th"
    if str_number.endswith('1') and not str_number.endswith('11'):
        suffix = 'st'
    elif str_number.endswith('2') and not str_number.endswith('12'):
        suffix = 'nd'
    elif str_number.endswith('3') and not str_number.endswith('13'):
        suffix = 'rd'

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
