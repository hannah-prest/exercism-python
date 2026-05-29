"""secret handshake"""
def commands(binary_str):
    """secret handshake"""
    actions = ["wink", "double blink", "close your eyes", "jump"]
    result = [action for action, digit in zip(actions, reversed(binary_str)) if digit == "1"]
    return result[::-1] if binary_str[0] == "1" else result