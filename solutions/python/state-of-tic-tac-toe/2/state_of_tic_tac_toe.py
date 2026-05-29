"""tictactoe"""
def gamestate(board):
    """tictactoe"""
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)
    if x_count - 2 == o_count:
        raise ValueError("Wrong turn order: X went twice")       
    if o_count - 1 == x_count:
        raise ValueError("Wrong turn order: O started")   
    
    win_patterns = [
        [(0,0), (0,1), (0,2)],  # top row
        [(1,0), (1,1), (1,2)],  # middle row
        [(2,0), (2,1), (2,2)],  # bottom row
        [(0,0), (1,0), (2,0)],  # left col
        [(0,1), (1,1), (2,1)],  # middle col
        [(0,2), (1,2), (2,2)],  # right col
        [(0,0), (1,1), (2,2)],  # diagonal
        [(0,2), (1,1), (2,0)],  # anti-diagonal
    ]
    is_winning = {"X": False, "O": False}
    is_full = True

    for pattern in win_patterns:
        player = board[pattern[0][0]][pattern[0][1]]
        if player != " " and all(board[r][c] == player for r, c in pattern):
            is_winning[player] = True
        if any(board[r][c] == " " for r, c in pattern):
            is_full = False
                    
    if not is_winning["X"] and not is_winning["O"]:
        if is_full:
            return "draw"
        return "ongoing"
    elif is_winning["X"] and is_winning["O"]:
        raise ValueError("Impossible board: game should have ended after the game was won")
    else:
        return "win"   