"""12 days of xmas"""
def recite(start_verse, end_verse):
    """12 days of xmas"""
    lines = (
        ("", ""),
        ("first", "a Partridge in a Pear Tree."),
        ("second", "two Turtle Doves, "),
        ("third", "three French Hens, "),
        ("fourth", "four Calling Birds, "),
        ("fifth", "five Gold Rings, "),
        ("sixth", "six Geese-a-Laying, "),
        ("seventh", "seven Swans-a-Swimming, "),
        ("eighth", "eight Maids-a-Milking, "),
        ("ninth", "nine Ladies Dancing, "),
        ("tenth", "ten Lords-a-Leaping, "),
        ("eleventh", "eleven Pipers Piping, "),
        ("twelfth", "twelve Drummers Drumming, ")
    )

    result = []
    for verse_number in range(start_verse, end_verse+1):
        verse = f"On the {lines[verse_number][0]} day of Christmas my true love gave to me: "
        for line_number in range(verse_number, 0, -1):
            final_line_and = "and " if verse_number > 1 and line_number == 1 else ""
            verse += f"{final_line_and}{lines[line_number][1]}"      
        result.append(verse)
        
    return result