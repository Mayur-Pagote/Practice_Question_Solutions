class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # Convert Celsius to Kelvin
        kelvin = celsius + 273.15
        
        # Convert Celsius to Fahrenheit
        fahrenheit = celsius * 1.80 + 32.00
        
        # Return both converted temperatures as a list
        return [kelvin, fahrenheit]
