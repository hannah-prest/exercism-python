"""Module for Bob's responses"""
def response(hey_bob):
    """Function for Bob's responses"""
    stripped_hey_bob = hey_bob.strip()
    if stripped_hey_bob == "":
        return "Fine. Be that way!"
    if stripped_hey_bob.endswith("?"):
        if stripped_hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure." 
    if stripped_hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."