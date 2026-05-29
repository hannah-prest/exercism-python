"""piglatin"""
def translate(text):
    """piglatin"""
    def first_vowel_index(text):
        vowels = "aeiouAEIOU"
        for index, char in enumerate(text):
            if char in vowels:
                return index
        return -1  # Return -1 if no vowel is found

    words = text.split(" ")
    piglatin = []
    for word in words:
        if word.startswith(("a","e","i","o","u","xr","yt")):
            piglatin.append(f"{word}ay")
        else:
            index_of_y = word.find("y")
            index_of_first_vowel = first_vowel_index(word)

            if index_of_y >= 0 and not word.startswith("y") and (index_of_first_vowel == -1 or index_of_y < index_of_first_vowel):
                index_of_first_vowel = index_of_y
                   
            start_of_word = word[:index_of_first_vowel]
            end_of_word = word[index_of_first_vowel:]
            if end_of_word.startswith("u") and start_of_word.endswith("q"):
                piglatin.append(f"{end_of_word[1:]}{start_of_word}uay")
            else:
                piglatin.append(f"{end_of_word}{start_of_word}ay")

    return " ".join(piglatin)
