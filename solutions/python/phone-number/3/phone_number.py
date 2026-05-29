"""phone number"""
import re
class PhoneNumber:
    """phone number"""
    def __init__(self, number):
        clean = re.sub(r"[+()-. ]", "", number)
            
        for char in clean:
            if char.isalpha():
                raise ValueError("letters not permitted")
            if not char.isdigit():
                raise ValueError("punctuations not permitted")
        
        if len(clean) < 10:
            raise ValueError("must not be fewer than 10 digits")
            
        if len(clean) > 11:
            raise ValueError("must not be greater than 11 digits")
            
        if len(clean) == 11:
            if clean[0] != "1":
                raise ValueError("11 digits must start with 1")
            clean = clean[1:]
            
        if clean[0] == "0":
            raise ValueError("area code cannot start with zero")
            
        if clean[0] == "1":
            raise ValueError("area code cannot start with one")
            
        if clean[3] == "0":
            raise ValueError("exchange code cannot start with zero")
            
        if clean[3] == "1":
            raise ValueError("exchange code cannot start with one")
            
        self.number = clean
        self.area_code = clean[0:3]

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
