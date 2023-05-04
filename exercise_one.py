"""Write a Temperature class that has a celsius property and a fahrenheit property.
The celsius property stores the temperature in Celsius, and the fahrenheit property stores the temperature in Fahrenheit.
The fahrenheit property should be a computed property that converts the Celsius temperature to Fahrenheit."""

from dataclasses import dataclass


@dataclass
class Temparature:
    _celsius: str

    @property
    def get_celsius(self):
        return self._celsius

    @get_celsius.setter
    def celsius(self, value: float):
        self._celsius = value

    @property
    def get_fahrenheit(self):
        return (self._celsius * 1.8) + 32


temparature = Temparature(28)
print(temparature.get_celsius)
print(temparature.get_fahrenheit)

temparature.celsius = 21
print(temparature.get_fahrenheit)
