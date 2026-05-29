"""clock"""
MINS_PER_HOUR = 60
MAX_HOUR = 24
class Clock:
    """clock"""
    
    def __init__(self, hour, minute):
        self._set_time(hour * MINS_PER_HOUR + minute)

    def _set_time(self, total_minutes):
        total_minutes = total_minutes % (MAX_HOUR * MINS_PER_HOUR)
        self.hour = total_minutes // MINS_PER_HOUR
        self.minute = total_minutes % MINS_PER_HOUR
    
    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self._set_time(self.hour * MINS_PER_HOUR + self.minute + minutes)
        return self
    
    def __sub__(self, minutes):
        self._set_time(self.hour * MINS_PER_HOUR + self.minute - minutes)
        return self
        