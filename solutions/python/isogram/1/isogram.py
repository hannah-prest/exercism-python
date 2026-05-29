"""isogram module"""
def is_isogram(string):
    """isogram function"""
    scrubbed_string = "".join(filter(str.isalpha, string.lower()))
    return len(set(scrubbed_string)) == len(scrubbed_string)