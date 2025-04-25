# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.


class TempratureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9
    
# Example usage:
celsius = 25
fahrenheit = TempratureConverter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit}°F")
fahrenheit = 77
celsius = TempratureConverter.fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is {celsius}°C")