"""module for multi color banded resistors"""
GIGA = 1000000000
MEGA = 1000000
KILO = 1000

def label(colors):
    """function for multi color banded resistors"""
    colors_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    number = (colors_list.index(colors[0]) * 10 + colors_list.index(colors[1])) * (10 ** colors_list.index(colors[2]))
    prefix = ""  
    if number >= GIGA:
        number = number // GIGA
        prefix = "giga"
    elif number >= MEGA:
        number = number // MEGA
        prefix = "mega"
    elif number >= KILO:
        number = number // KILO
        prefix = "kilo"
    return f"{number} {prefix}ohms"
