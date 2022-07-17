# Базовый класс фигуры

class Figure:
    name = 'Figure'

    def __init__(self, *side):
        self.side = side

    @property
    def perimeter(self):
        return sum(self.side)

    def add_area(self, figure):
        if 'Figure' in str(figure.__class__.__mro__):
            return round(self.area + figure.area, 2)
        else:
            raise ValueError
