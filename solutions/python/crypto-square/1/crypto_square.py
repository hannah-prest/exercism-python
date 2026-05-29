"""cipher"""
import math
def cipher_text(plain_text):
    """cipher"""
    clean_text = "".join(char.lower() for char in plain_text if char.isalnum())
    cols = math.ceil(math.sqrt(len(clean_text)))
    if cols == 0:
        return ""
        
    rows = math.ceil(len(clean_text) / cols)
    chunks = [clean_text[i:i+cols].ljust(cols) for i in range(0, len(clean_text), cols)]
    transposed = ["".join(r) for r in zip(*chunks)]
    return " ".join(transposed)