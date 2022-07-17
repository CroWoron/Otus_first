# Класс окружности.
from math import pi
from src.Figure import Figure


class Circle(Figure):
    """Класс окружности

    Задается радиусом"""
    name = 'Circle'

    @property
    def radius(self):
        return sum(self.side)

    @property
    def area(self):
        return round(pi * self.radius ** 2, 2)

    @property
    def perimeter(self):
        return round(2 * pi * self.radius, 2)
