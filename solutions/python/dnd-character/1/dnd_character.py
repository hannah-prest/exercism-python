"""dnd"""
import random
class Character:
    """dnd"""
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + ((self.constitution - 10)//2)

    def ability(self):
        rolls = [random.randint(1, 6) for _ in range(4)]
        return sum(sorted(rolls)[1:])

def modifier(value):
    """dnd"""
    return (value - 10)//2
