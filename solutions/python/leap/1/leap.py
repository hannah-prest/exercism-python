def leap_year(year):
    evenly_divisible_by_4 = year % 4 == 0
    evenly_divisible_by_100 = year % 100 == 0
    evenly_divisible_by_400 = year % 400 == 0
    return evenly_divisible_by_4 and (not evenly_divisible_by_100 or evenly_divisible_by_400)