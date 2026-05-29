"""dominoes"""
def can_chain(dominoes):
    """dominoes"""
    if len(dominoes) == 0:
        return []
    
    def search(remaining, chain):
        if len(remaining) == 0:
            return chain if chain[0][0] == chain[-1][1] else None
        
        for index, domino in enumerate(remaining):
            next_remaining = [rd for i, rd in enumerate(remaining) if i != index]
            for candidate in [domino, domino[::-1]]:
                if candidate[0] == chain[-1][1]:
                    result = search(next_remaining, chain + [candidate])
                    if result is not None:
                        return result
        return None
    
    for index, domino in enumerate(dominoes):
        remaining = [rd for i, rd in enumerate(dominoes) if i != index]
        for candidate in [domino, domino[::-1]]:
            result = search(remaining, [candidate])
            if result is not None:
                return result
    
    return None