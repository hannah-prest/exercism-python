"""matrix"""
class Matrix:
    """matrix"""
    def __init__(self, matrix_string):
        rows = matrix_string.split("\n")
        self.value = [[int(digit) for digit in chars.split(" ")] for chars in rows]

    def row(self, index):
        return self.value[index-1]

    def column(self, index):
        return [row[index-1] for row in self.value]
