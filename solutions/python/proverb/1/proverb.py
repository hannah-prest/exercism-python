"""proverb"""
def proverb(*items, qualifier=""):
    """proverb"""
    lines = []
    
    if len(items) > 1:
        for index in range(0, len(items)-1):
            lines.append(f"For want of a {items[index]} the {items[index+1]} was lost.")

    if len(items) > 0:
        final = items[0] if qualifier is None else f"{qualifier} {items[0]}"
        lines.append(f"And all for the want of a {final}.")
    return lines