"""anagrams"""
def find_anagrams(word, candidates):
    """anagrams"""
    word_lower = word.lower()
    word_sorted = sorted(word_lower)
    return [
        cand for cand in candidates
        if cand.lower() != word_lower
        and sorted(cand.lower()) == word_sorted
    ]
