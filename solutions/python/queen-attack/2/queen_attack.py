"""chess"""
BOARD_MIN = 0
BOARD_MAX = 7
class Queen:
    """queen"""
    def __init__(self, row, column):
        if row < BOARD_MIN:
            raise ValueError("row not positive")
            
        if row > BOARD_MAX:
            raise ValueError("row not on board")
            
        if column < BOARD_MIN:
            raise ValueError("column not positive")
            
        if column > BOARD_MAX:
            raise ValueError("column not on board")
            
        self.row = row
        self.column = column
            

    def can_attack(self, another_queen):
        """can queens attack"""
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")
        row_diff = abs(self.row - another_queen.row)
        col_diff = abs(self.column - another_queen.column)
        return (self.row == another_queen.row or 
                self.column == another_queen.column or 
                row_diff == col_diff)
