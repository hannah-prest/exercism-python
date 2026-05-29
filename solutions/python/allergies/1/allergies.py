"""allergies"""
ALLERGENS = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128,
}

class Allergies:
    """allerigies"""
    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return self.score & ALLERGENS[item] >= 1

    @property
    def lst(self):
        return [a for a in ALLERGENS if self.allergic_to(a)]
