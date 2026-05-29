"""Module for calculating age in years on planets from seconds"""
class SpaceAge:
    """Class for calculating age in years on planets from seconds"""
    def __init__(self, seconds):
        self.seconds = seconds

    def calculate(self, orbital_period_in_earth_years):
        earth_days_in_year = 365.25
        local_days_in_year = orbital_period_in_earth_years * earth_days_in_year
        local_year_in_seconds = 60 * 60 *24 * local_days_in_year
        return round(self.seconds / local_year_in_seconds, 2)
    
    def on_earth(self):
        return self.calculate(1.0)
    
    def on_mercury(self):
        return self.calculate(0.2408467)
    
    def on_venus(self):
        return self.calculate(0.61519726)
    
    def on_mars(self):
        return self.calculate(1.8808158)
    
    def on_jupiter(self):
        return self.calculate(11.862615)
    
    def on_saturn(self):
        return self.calculate(29.447498)
    
    def on_uranus(self):
        return self.calculate(84.016846)
    
    def on_neptune(self):
        return self.calculate(164.79132)