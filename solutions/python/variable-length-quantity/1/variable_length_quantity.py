"""VLQ"""
def encode(numbers):
    """VLQ"""
    result = []
    for num in numbers:        
        bytes_out = [num & 0x7F] 
        num >>= 7                  
        while num > 0:
            bytes_out.append((num & 0x7F) | 0x80) 
            num >>= 7
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
