"""DNA to RNA"""
def to_rna(dna_strand):
    """DNA to RNA"""
    matching = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return "".join(matching[dna] for dna in dna_strand)