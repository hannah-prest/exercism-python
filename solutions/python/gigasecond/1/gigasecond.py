"""gigasecond"""
from datetime import datetime, timedelta
GIGASECOND = 1_000_000_000
def add(moment):
    """gigasecond"""
    return moment + timedelta(seconds=GIGASECOND)
