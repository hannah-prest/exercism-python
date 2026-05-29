"""module for multi color banded resistors"""
def value(colors):
    """function for multi color banded resistors"""
    colors_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    return colors_list.index(colors[0]) * 10 + colors_list.index(colors[1])
