"""module for multi color banded resistors"""
GIGA = 1000000000
MEGA = 1000000
KILO = 1000

def resistor_label(colors):
    """function for multi color banded resistors"""
    colors_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    number = 0
    if len(colors) == 1:
        number = colors_list.index(colors[0])
    if len(colors) >= 2:
        number = colors_list.index(colors[0]) * 10 + colors_list.index(colors[1])  
    if len(colors) == 5:
        number = colors_list.index(colors[0]) * 100 + colors_list.index(colors[1]) * 10 + colors_list.index(colors[2])
        
    prefix = ""  
    if len(colors) >= 3:
        number *= (10 ** colors_list.index(colors[-2]))
        if number >= GIGA:
            number = number // GIGA if number % GIGA == 0 else number / GIGA
            prefix = "giga"
        elif number >= MEGA:
            number = number // MEGA if number % MEGA == 0 else number / MEGA
            prefix = "mega"
        elif number >= KILO:
            number = number // KILO if number % KILO == 0 else number / KILO
            prefix = "kilo"

    tolerance = ""
    if len(colors) >= 4:
        tolerance_list = {
            "grey": "±0.05%",
            "violet": "±0.1%",
            "blue": "±0.25%",
            "green": "±0.5%",
            "brown": "±1%",
            "red": "±2%",
            "gold": "±5%",
            "silver": "±10%"
        }
        tolerance = tolerance_list[colors[-1]]
    
    return f"{number} {prefix}ohms {tolerance}".strip()