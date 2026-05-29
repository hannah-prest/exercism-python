"""sum of multiples"""
def sum_of_multiples(limit, multiples):
    """sum of multiples"""
    if limit == 1:
        return 0
        
    multiples_set = set()
    for number in multiples:
        multiples_set = multiples_set | set(number * i for i in range(1, limit + 1) if number * i < limit)

    return sum(multiples_set)
