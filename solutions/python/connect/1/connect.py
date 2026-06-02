"""Hex game"""
PLYR_O = "O"
PLYR_X = "X"

class ConnectGame:
    """game"""
    def __init__(self, board):
        self.board = HexMatrix(board)

    def player_o_wins(self, row, col):
        return row == self.board.height - 1
    
    def player_x_wins(self, row, col):
        return col == self.board.width - 1 + row

    def get_winner(self):
        winner = ""
        if any(char == PLYR_O for char in self.board.row(0)) and any(char == PLYR_O for char in self.board.row(self.board.height - 1)):
            first_cells = [(0,c) for c in range(self.board.width) if self.board.value[0][c] == PLYR_O]
            winner = self.trace_player(PLYR_O, first_cells, self.player_o_wins)
        if winner == "" and any(char == PLYR_X for char in self.board.column(0)) and any(char == PLYR_X for char in self.board.column(self.board.width - 1)):
            first_cells = [(r,0+r) for r in range(self.board.height) if self.board.value[r][r] == PLYR_X]
            winner = self.trace_player(PLYR_X, first_cells, self.player_x_wins)
        return winner

    def trace_player(self, player, seeds, win_condtion):
        visited  = set()
        stack = seeds
        while stack:
            current = stack.pop()
            row = current[0]
            col = current[1]
            if self.board.value[row][col] == player:
                if win_condtion(row, col):
                    return player
                visited .add(current)
                potential = [(r,c) for r,c in self.board.get_neighbor_coords(row,col) if self.board.value[r][c] == player and (r,c) not in visited ]
                visited .update(potential)
                stack.extend(potential)                  
        return ""

class HexMatrix:
    """Hex matrix"""
    def __init__(self, matrix_string):
        rows = matrix_string.splitlines()
        target_len = len(rows[0])
        offset = 0
        self.value = []
        for row in rows:
            drop_count = max(0, len(row) - target_len)
            cleaned = row[drop_count-offset:]
            self.value.append([char for char in cleaned])
            offset+=1
            
    def __str__(self):            
        return "\n".join("".join(row) for row in self.value)

    def get_neighbor_coords(self, row, col):
        offsets = [ (-1,-1), (-1,1),
                  (0,-2),        (0,2),
                    (1,-1),  (1,1)]
        return [(row + dr,col + dc)
            for dr, dc in offsets
            if 0 <= row + dr < self.height
                and 0 <= col + dc < len(self.value[row])]

    def row(self, index):
        return self.value[index]

    def column(self, index):
        return [row[index+offset] for offset, row in enumerate(self.value)]

    @property
    def height(self):
        return len(self.value)

    @property
    def width(self):
        return len(self.value[0])