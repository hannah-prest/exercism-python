"""list ops"""

def append(list1, list2):
    """append"""
    return list1 + list2

def concat(lists):
    """concat"""
    result = []
    for list in lists:
        result += list
    return result

def filter(function, list):
    """filter"""
    return [item for item in list if function(item)]

def length(list):
    """length"""
    return len(list)

def map(function, list):
    """map"""
    return [function(item) for item in list]

def foldl(function, list, initial):
    """foldl"""
    result = initial
    for item in list:
        result = function(result,item)
    return result

def foldr(function, list, initial):
    """foldr"""
    result = initial
    for item in list[::-1]:
        result = function(result,item)
    return result

def reverse(list):
    """reverse"""
    return list[::-1]