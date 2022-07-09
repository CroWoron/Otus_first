# Базовый класс фигуры

class Figure:
    def __init__(self, side):
        self.side = side
        self.name = 'Базовая фигура'
        self.area = None
        if self.side <= 0:
            raise ValueError

    def add_area(self, figure):
        return figure.area + self.area
