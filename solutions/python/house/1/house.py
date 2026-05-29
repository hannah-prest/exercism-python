"""the house that jack built"""
def recite(start_verse, end_verse):
    """the house that jack built"""
    nouns = ["the house", "the malt", "the rat", "the cat", "the dog","the cow with the crumpled horn","the maiden all forlorn","the man all tattered and torn","the priest all shaven and shorn","the rooster that crowed in the morn"
             ,"the farmer sowing his corn","the horse and the hound and the horn"]
    clauses = ["Jack built.","lay in","ate","killed","worried","tossed","milked","kissed","married","woke","kept","belonged to"]
    poem_parts = list(zip(nouns, clauses))
    result = []
    for index in range(start_verse-1, end_verse):
        line = "This is"   
        for noun, clause in reversed(poem_parts[:index+1]):      
            line += f" {noun} that {clause}"
        result.append(line)
    return result