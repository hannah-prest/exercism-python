"""flatten array"""
def flatten_gen(nested_list):
    """yields elements from a nested list"""
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_gen(item)
        elif item is not None:
            yield item
    
def flatten(iterable):
    """flatten array"""
    return list(flatten_gen(iterable))