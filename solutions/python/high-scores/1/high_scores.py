"""score track"""
class HighScores:
    """score track"""
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def descending(self):
        return list(reversed(sorted(self.scores)))

    def personal_best(self):
        return self.descending()[0]

    def personal_top_three(self):
        return self.descending()[0:3]
