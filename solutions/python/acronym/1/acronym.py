"""Acronym"""
import re
import string
def abbreviate(words):
    """Acronym"""
    clean_text = "".join(c for c in words if c not in string.punctuation or c == '-')
    seperated = re.split(r'[\s-]+', clean_text)
    return "".join([w[0] for w in seperated]).upper()