"""say number in english"""
DIGITS = [
    ["zero", "", ""],
    ["one", "eleven", "ten"],
    ["two", "twelve", "twenty"],
    ["three", "thirteen", "thirty"],
    ["four", "fourteen", "forty"],
    ["five", "fifteen", "fifty"],
    ["six", "sixteen", "sixty"],
    ["seven", "seventeen", "seventy"],
    ["eight", "eighteen", "eighty"],
    ["nine", "nineteen", "ninety"],
]

POSITIONS = [" billion", " million", " thousand", ""]

def say(number):
    """say number in english"""
    if number < 0:
        raise ValueError("input out of range")

    if number > 999_999_999_999:
        raise ValueError("input out of range")

    number_as_string = str(number).zfill(12)
    chunks = [number_as_string[i:i+3] for i in range(0, len(number_as_string), 3)]
    result = ""
    for pos, chunk in enumerate(chunks):
        if int(chunk) > 0:
            word = POSITIONS[pos]
            hundreds, tens, ones = map(int, chunk)
            if hundreds >= 1:
                result += f" {DIGITS[hundreds][0]} hundred"
            if tens >= 1 and (ones == 0 or tens >= 2):
                result += f" {DIGITS[tens][2]}"
            if ones >= 1:
                prefix = "-" if tens >= 2 else " "
                grab_teen_or_ones = int(tens == 1) 
                result += f"{prefix}{DIGITS[ones][grab_teen_or_ones]}"
            result += word

    if len(result) == 0:
        return DIGITS[0][0]

    return result.strip()