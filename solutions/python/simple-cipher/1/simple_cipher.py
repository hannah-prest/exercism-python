"""Vigenère cipher"""
import string
import secrets
from itertools import cycle
ALPHABET_LEN = 26
class Cipher:
    """Vigenère cipher"""
    def __init__(self, key=None):
        if key is None:
            key = ''.join(secrets.choice(string.ascii_lowercase) for i in range(100))
        self.key = key


    def encode(self, text):
        return ''.join(
            string.ascii_lowercase[(string.ascii_lowercase.index(c) + string.ascii_lowercase.index(k)) % ALPHABET_LEN]
            for c, k in zip(text, cycle(self.key))
        )

    def decode(self, text):
        return ''.join(
            string.ascii_lowercase[(string.ascii_lowercase.index(c) - string.ascii_lowercase.index(k)) % ALPHABET_LEN]
            for c, k in zip(text, cycle(self.key))
        )
