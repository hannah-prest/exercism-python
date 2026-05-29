"""Fewest Coins"""
def find_fewest_coins(coins, target):
    """Fewest Coins"""
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    if not any(c <= target for c in coins):
        raise ValueError("can't make target with given coins")
        
    breakdown_for = [None] * (target + 1)
    breakdown_for[0] = []

    sub_targets = range(1, target+1)
    for value in sub_targets:
        for coin in coins:
            remainder = value - coin
            if coin <= value and breakdown_for[remainder] is not None:
                possibility = breakdown_for[remainder] + [coin]
                if breakdown_for[value] is None or len(possibility) < len(breakdown_for[value]):
                    breakdown_for[value] = possibility
    
    if breakdown_for[target] is None:
        raise ValueError("can't make target with given coins")

    return sorted(breakdown_for[target])