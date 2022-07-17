#Класс для треугольника

from src.Figure import Figure


class Triangle(Figure):
    """Класс треугольника

    Задается тремя сторонами, если передано неверное количество сторон,
    или из за их длинны невозможно создать треугольник возвращает исключение"""
    name = 'Triangle'

    def __init__(self, *side):
        self.side = side
        if len(self.side) != 3:
            raise ValueError
        self.a, self.b, self.c = (self.side)
        if not self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            raise ValueError
        if self.a == 0 or self.b == 0 or self.c == 0:
            raise ValueError

    @property
    def area(self):
        p = self.perimeter * 0.5  # Половина периметра для выполнения Формулы Герона
        S = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5  # Формула Герона
        return round(S, 1)
