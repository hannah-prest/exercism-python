"""atbash cipher"""
import string

PLAIN = string.ascii_lowercase
CIPHER = PLAIN[::-1]
ENCODE_TABLE = str.maketrans(PLAIN + string.digits, CIPHER + string.digits)
DECODE_TABLE = str.maketrans(CIPHER + string.digits, PLAIN + string.digits)

def encode(plain_text):
    """encode atbash cipher"""
    cleaned = "".join(char.lower() for char in plain_text if char.isalpha() or char.isdigit())
    translation = cleaned.translate(ENCODE_TABLE)
    return " ".join(translation[index:index+5] for index in range(0, len(translation), 5))


def decode(ciphered_text):
    """decode atbash cipher"""
    cleaned = "".join(char.lower() for char in ciphered_text if char.isalpha() or char.isdigit())
    return cleaned.translate(DECODE_TABLE)