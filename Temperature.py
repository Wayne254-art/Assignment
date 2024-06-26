

class Temperature:
    def convertFahrenheit(self, celsius):
        """Convert Celsius to Fahrenheit and print the result."""
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is {fahrenheit}°F")

    def convertCelsius(self, fahrenheit):
        """Convert Fahrenheit to Celsius and print the result."""
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius}°C")

temp = Temperature()
temp.convertFahrenheit(25) 
temp.convertCelsius(77)     
