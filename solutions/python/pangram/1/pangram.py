"""Is Pangram module"""
import string
def is_pangram(sentence):
    """Is Pangram function"""
    return all(letter in sentence.lower() for letter in string.ascii_lowercase)