"""VLQ"""
def encode(numbers):
    """VLQ"""
    result = []
    for item in numbers:        
        bytes_out = [item & 0x7F] 
        item >>= 7                  
        while item > 0:
            bytes_out.append((item & 0x7F) | 0x80) 
            item >>= 7
        result += list(reversed(bytes_out))
    return result


def decode(bytes_):
    """VLQ"""
    result = []
    current = 0

    for byte in bytes_:
        current = (current << 7) | (byte & 0x7F)
        if not (byte & 0x80):                
            result.append(current)
            current = 0 

    if bytes_ and (bytes_[-1] & 0x80):
        raise ValueError("incomplete sequence")

    return result
