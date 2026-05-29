"""RNA"""
METHIONINE = "Methionine"
PHENYLALANINE = "Phenylalanine"
LEUCINE = "Leucine"
SERINE = "Serine"
TYROSINE = "Tyrosine"
CYSTEINE = "Cysteine"
TRYPTOPHAN = "Tryptophan"
STOP = "STOP"

CODONS = {
    "AUG": METHIONINE,
    "UUU": PHENYLALANINE, "UUC": PHENYLALANINE,
    "UUA": LEUCINE, "UUG": LEUCINE,
    "UCU": SERINE, "UCC": SERINE, "UCA": SERINE, "UCG": SERINE,
    "UAU": TYROSINE, "UAC": TYROSINE,
    "UGU": CYSTEINE, "UGC": CYSTEINE,
    "UGG": TRYPTOPHAN,
    "UAA": STOP, "UAG": STOP, "UGA": STOP,
}

SEQUENCE_LENGTH = 3
def proteins(strand):
    """RNA"""
    result = []
    for iterator in range(0,len(strand),SEQUENCE_LENGTH):
        sequence = strand[iterator:iterator+SEQUENCE_LENGTH]
        amino_acid = CODONS[sequence]
        if amino_acid == STOP:
            break
        result.append(amino_acid)
    return result
