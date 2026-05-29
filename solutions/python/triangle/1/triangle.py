"""Module to detemine if sides are a type of triangle"""
def is_triangle(sides):
    if sides[0] == 0 or sides[2] == 0 or sides[1] == 0:
        return False
    if len(sides) != 3:
        return False
    if (sides[0] + sides[1]) >= sides[2] and (sides[2] + sides[1]) >= sides[0] and (sides[0] + sides[2]) >= sides[1]:
        return True
    return False   

def equilateral(sides):
    if is_triangle(sides):
        return sides[0] == sides[1] == sides[2]
    return False

def isosceles(sides):
    if is_triangle(sides):
        return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]
    return False


def scalene(sides):
    return is_triangle(sides) and not equilateral(sides) and not isosceles(sides)
