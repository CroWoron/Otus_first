# Класс для квадрата

from src.Figure import Figure


class Square(Figure):
    """Класс квадрата

    Задается одной стороной
    """
    name = 'Square'

    @property
    def area(self):
        return sum(self.side) ** 2

    @property
    def perimeter(self):
        return sum(self.side) * 4
