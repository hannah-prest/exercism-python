"""killer sudoku cage calculations"""
from itertools import combinations as iter_combinations
def combinations(target, size, exclude):
    """killer sudoku cage calculations"""
    combos = list(iter_combinations(range(1,10), size))
    return [list(combo) for combo in combos if all(c not in exclude for c in combo) and sum(combo) == target]