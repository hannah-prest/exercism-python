"""dnd"""
import random
class Character:
    """dnd"""
    def __init__(self):
        self.strength = random_ability_score()
        self.dexterity = random_ability_score()
        self.constitution = random_ability_score()
        self.intelligence = random_ability_score()
        self.wisdom = random_ability_score()
        self.charisma = random_ability_score()
        self.hitpoints = 10 + ((self.constitution - 10)//2)

    def ability(self):
        abilities = [self.strength, self.dexterity, self.constitution, 
                     self.intelligence, self.wisdom, self.charisma]
        return random.choice(abilities)

def random_ability_score():
    rolls = [random.randint(1, 6) for _ in range(4)]
    return sum(sorted(rolls)[1:])

def modifier(value):
    """dnd"""
    return (value - 10)//2
