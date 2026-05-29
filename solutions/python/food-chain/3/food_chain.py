"""old lady"""
from collections import namedtuple
def recite(start_verse, end_verse):
    """old lady"""
    end_line = "I don't know why she swallowed the fly. Perhaps she'll die."
    Animal = namedtuple('Animal', ['name', 'comment', 'qualifier'])
    lines = (
        Animal("", "", ""),
        Animal("fly", "", ""),
        Animal("spider", "It wriggled and jiggled and tickled inside her.", " that wriggled and jiggled and tickled inside her"),
        Animal("bird", "How absurd to swallow a bird!", ""),
        Animal("cat", "Imagine that, to swallow a cat!", ""),
        Animal("dog", "What a hog, to swallow a dog!", ""),
        Animal("goat", "Just opened her throat and swallowed a goat!", ""),
        Animal("cow", "I don't know how she swallowed a cow!", ""),
        Animal("horse", "She's dead, of course!", "")
    )

    verses = []
    for verse_number in range(start_verse, end_verse+1):
        if verse_number > start_verse:
            verses.append("")
        animal = lines[verse_number]
        verses.append(f"I know an old lady who swallowed a {animal.name}.")
        if verse_number > 1:
            verses.append(animal.comment)
        if animal.name == "horse":
            break
        for line_number in range(verse_number, 1, -1):
            line_animal = lines[line_number]
            next_line_animal = lines[line_number-1]
            verses.append(f"She swallowed the {line_animal.name} to catch the {next_line_animal.name}{next_line_animal.qualifier}.")
        verses.append(end_line)
    
    return verses