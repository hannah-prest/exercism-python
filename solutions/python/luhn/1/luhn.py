"""Luhn"""
class Luhn:
    """Luhn"""
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        """validate"""
        doubled = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
        cleaned = self.card_num.replace(" ", "")
        if len(cleaned) <= 1 or not cleaned.isdigit():
            return False
        total = sum(
            doubled[int(d)] if i % 2 == 1 else int(d)
            for i, d in enumerate(reversed(cleaned))
        )
        return total % 10 == 0