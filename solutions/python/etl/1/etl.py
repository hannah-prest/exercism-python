"""transform"""
def transform(legacy_data):
    """transform"""
    return {letter.lower(): score for score, letters in legacy_data.items() for letter in letters}