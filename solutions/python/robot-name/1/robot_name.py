"""robot"""
import random
import string

_used_names = set()

def _generate_name():
    while True:
        name = (random.choice(string.ascii_uppercase) + 
                random.choice(string.ascii_uppercase) + 
                str(random.randint(100, 999)))
        if name not in _used_names:
            _used_names.add(name)
            return name

class Robot:
    """robot"""
    def __init__(self):
        self._name = None

    @property
    def name(self):
        if self._name is None:
            self._name = _generate_name()
        return self._name
       
    def reset(self):
        self._name = None