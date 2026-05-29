"""Darts game scoring module"""
def score(x, y):
    """Darts game scoring function"""
    calculated = x**2 + y**2
    if calculated <= 1:
        return 10
    if calculated <= 5**2:
        return 5
    if calculated <= 10**2:
        return 1
    return 0
