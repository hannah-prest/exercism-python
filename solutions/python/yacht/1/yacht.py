"""yacht"""
from collections import Counter
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

def full_house(dice):
    """score full house"""
    counts = dice.most_common()
    if len(counts) == 2 and counts[0][1] == 3:
        return sum_dice(dice)
    return 0

def score_single(dice, value):
    """score occurance of a dice"""
    return dice.get(value, 0) * value

def sum_dice(dice):
    return sum(v * c for v, c in dice.items())

SCORES = {
    YACHT: lambda dice: 50 if len(dice) == 1 else 0,
    ONES: lambda dice: score_single(dice,1),
    TWOS: lambda dice: score_single(dice,2),
    THREES: lambda dice: score_single(dice,3),
    FOURS: lambda dice: score_single(dice,4),
    FIVES: lambda dice: score_single(dice,5),
    SIXES: lambda dice: score_single(dice,6),
    FULL_HOUSE: full_house,
    FOUR_OF_A_KIND: lambda dice: next((v * 4 for v, c in dice.most_common() if c >= 4), 0),
    LITTLE_STRAIGHT: lambda dice: 30 if dice == Counter([1,2,3,4,5]) else 0,
    BIG_STRAIGHT: lambda dice: 30 if dice == Counter([2,3,4,5,6]) else 0,
    CHOICE: sum_dice,
}

def score(dice, category):
    """score for category"""
    dice_cc = Counter(dice)
    return SCORES[category](dice_cc)
     