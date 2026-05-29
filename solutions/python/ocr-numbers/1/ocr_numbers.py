"""ocr"""
def convert(input_grid):
    """ocr"""
    height = len(input_grid)
    if height % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    width = 0 if height == 0 else len(input_grid[0])
    if width % 3 != 0 or any(len(row) != width for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")
    valid_chars = {"|", "_", " "}
    if any(set(row) - valid_chars for row in input_grid):
        raise ValueError("The input is invalid with current characters.")
    
    def parse_cell(matrix):
        patterns = {
            (True,  False, True,  True,  True,  True,  True ): "0",
            (False, False, False, False, True,  False, True  ): "1",
            (True,  True,  True, False, True,  True,  False ): "2",
            (True,  True,  True, False, True,  False, True  ): "3",
            (False, True,  False, True,  True,  False, True  ): "4",
            (True,  True,  True, True,  False, False, True  ): "5",
            (True,  True,  True,  True,  False, True, True  ): "6",
            (True,  False, False, False, True,  False, True  ): "7",
            (True,  True,  True,  True,  True,  True,  True  ): "8",
            (True,  True,  True, True,  True,  False, True  ): "9",
        }
        top      = cell[0][1] == "_"  # top row, middle char
        middle   = cell[1][1] == "_"  # middle row, middle char
        bottom   = cell[2][1] == "_"  # bottom row, middle char
        top_left  = cell[1][0] == "|"  # middle row, left char
        top_right = cell[1][2] == "|"  # middle row, right char
        bot_left  = cell[2][0] == "|"  # bottom row, left char
        bot_right = cell[2][2] == "|"  # bottom row, right char
        key = (top, middle, bottom, top_left, top_right, bot_left, bot_right)
        return patterns.get(key, "?")

    result = []
    for row_i in range(0, height, 4):
        number_line = ""
        for col_i in range(0, width, 3):
            cell = [row[col_i:col_i+3] for row in input_grid[row_i:row_i+4]]       
            number_line += str(parse_cell(cell))
        result.append(number_line)
    
    return ",".join(result)