"""count rectangles"""
VALID_ROW = {"+","-"}
VALID_COL = {"+","|"}

def _is_rectangle(strings, top, bottom, left, right):
    """check all four sides of a candidate rectangle"""
    return (strings[bottom][left] == "+" 
            and strings[bottom][right] == "+"
            and all(strings[top][c] in VALID_ROW for c in range(left, right+1))
            and all(strings[bottom][c] in VALID_ROW for c in range(left, right+1))
            and all(strings[r][left] in VALID_COL for r in range(top, bottom+1))
            and all(strings[r][right] in VALID_COL for r in range(top, bottom+1)))

def _corner_positions(row, before):
    """yield indices of '+' characters before a given column"""
    return (i for i, c in enumerate(row[:before]) if c == "+")

def rectangles(strings):
    """count rectangles"""
    return sum(1 
               for top, row in enumerate(strings)
               for right, char in enumerate(row) if char == "+"
               for left in _corner_positions(row, right)
               for bottom in range(top+1, len(strings))
               if _is_rectangle(strings, top, bottom, left, right)
              )