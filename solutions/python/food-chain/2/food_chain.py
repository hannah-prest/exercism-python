"""old lady"""
def recite(start_verse, end_verse):
    """old lady"""
    end_line = "I don't know why she swallowed the fly. Perhaps she'll die."

    lines = (
        ("", "", ""),
        ("fly", "", ""),
        ("spider", "It wriggled and jiggled and tickled inside her.", " that wriggled and jiggled and tickled inside her"),
        ("bird", "How absurd to swallow a bird!", ""),
        ("cat", "Imagine that, to swallow a cat!", ""),
        ("dog", "What a hog, to swallow a dog!", ""),
        ("goat", "Just opened her throat and swallowed a goat!", ""),
        ("cow", "I don't know how she swallowed a cow!", ""),
        ("horse", "She's dead, of course!", "")
    )

    verses = []
    for verse_number in range(start_verse, end_verse+1):
        animal = lines[verse_number]
        verses.append(f"I know an old lady who swallowed a {animal[0]}.")
        if verse_number > 1:
            verses.append(animal[1])
        is_horse = verse_number == 8
        if is_horse:
            break
        for line_number in range(verse_number, 1, -1):
            line_animal = lines[line_number]
            next_line_animal = lines[line_number-1]
            verses.append(f"She swallowed the {line_animal[0]} to catch the {next_line_animal[0]}{next_line_animal[2]}.")
        verses.append(end_line)
        if verse_number+1 <= end_verse:
            verses.append("")
    
    return verses