"""Module for resistor colors"""
def color_code(color):
    """function to get the numerical value for a color"""
    return colors().index(color)


def colors():
    """function to list all colors for resistor bands"""
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
