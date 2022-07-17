# Класс для прямоугольника.

from src.Figure import Figure


class Rectangle(Figure):
    """Класс прямоугольника

    Прямоугольник задается двумя сторонами."""
    name = 'Rectangle'

    @property
    def area(self):
        if len(self.side) == 2:
            a, b = (self.side)
            return a * b
        else:
            raise ValueError

    @property
    def perimeter(self):
        return sum(self.side) * 2
