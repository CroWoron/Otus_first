# Класс для квадрата

from Figure import Figure


class Square(Figure):
    def __init__(self, side):
        super().__init__(side)
        self.name = 'Square'
        self.area = side ** 2
        self.perimeter = 4 * side
