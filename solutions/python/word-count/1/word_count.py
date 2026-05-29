"""count words"""
import re
def count_words(sentence):
    """count words"""
    words = re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)*", sentence.lower())
    result = {}

    for word in words:
        result.setdefault(word, 0)
        result[word] += 1

    return result