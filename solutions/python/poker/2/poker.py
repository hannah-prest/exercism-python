"""poker best hands"""
from collections import Counter

class Hand:
    """Hand class for helping with calculations"""
    def __init__(self, cards: list[str], values: Counter[int], suits: Counter[str]):
        self.cards = cards
        self.values = values
        self.suits = suits

    def is_sequential(self):
        return len(self.values) == (max(self.values) - min(self.values) + 1)

    def is_one_suit(self):
        return len(self.suits) == 1

def n_of_a_kind(n: int, hand: Hand, base_points: int, double_ocurance=False):
    """calculates score for pair (2 of a kind), 3 of a kind, 4 of a kind, etc as well as 2 pair (2 sets of 2 of a kind)"""
    most_common = sorted(hand.values.most_common(), key=lambda x: (x[1], x[0]), reverse=True)
    most_common_value, most_common_count = most_common[0]
    kickers = [v for v, c in most_common[1:]]
    if most_common_count == n and (not double_ocurance or most_common[1][1] == n):
        return (base_points, most_common_value, *kickers)
    return None

def straight(hand: Hand):
    """calculates score for straight"""
    values = set(hand.values)
    if values == {14, 2, 3, 4, 5}:
        return (4, 5)  # 5 is the high card for a low straight
    if hand.is_sequential():
        return (4, max(hand.values))
    return None

def flush(hand: Hand):
    """calculates score for flush"""
    if not hand.is_sequential() and hand.is_one_suit():
        return (5, *sorted(hand.values, reverse=True))
    return None

def full_house(hand: Hand):
    """calculates score for full house"""
    most_common_value, most_common_count = hand.values.most_common()[0]
    next_common_value, next_common_count = hand.values.most_common()[1]
    if most_common_count == 3 and next_common_count == 2:
        return (6, most_common_value, next_common_value)
    return None

def straight_flush(hand: Hand):
    """calculates score for straight flush and royal flush"""
    values = set(hand.values)
    if values == {14, 2, 3, 4, 5} and hand.is_one_suit():
        return (8, 5)  # 5 is the high card for a low straight flush
    if hand.is_sequential() and hand.is_one_suit():
        return (8, max(hand.values))
    return None

COMBOS = [
    lambda hand: (0, *sorted(hand.values, reverse=True)),
    lambda hand: n_of_a_kind(2, hand, 1),
    lambda hand: n_of_a_kind(2, hand, 2, True),
    lambda hand: n_of_a_kind(3, hand, 3),
    straight,
    flush,
    full_house,
    lambda hand: n_of_a_kind(4, hand, 7),
    straight_flush,
]

def value_as_numeric(card_value):
    """get numeric values of cards"""
    if card_value == "K":
        return 13
    if card_value == "Q":
        return 12
    if card_value == "J":
        return 11
    if card_value == "A":
        return 14 #14 is best in almost all scenarios
    return int(card_value)

def score_hand(hand: str):
    """runs hand through all scoring possibilities"""
    cards = hand.split(" ")
    values = Counter([value_as_numeric(card[:-1]) for card in cards])
    suits = Counter([card[-1] for card in cards])
    nt_hand = Hand(cards, values, suits)
    for combo in reversed(COMBOS):
        score = combo(nt_hand)
        if score is not None:
            return score
    return None

def best_hands(hands):
    """poker best hands"""
    scores = [(score_hand(hand), hand) for hand in hands]
    best_score = max(scores)[0]
    return [hand for score, hand in scores if score == best_score]