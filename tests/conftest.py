import pytest
from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle


@pytest.fixture
def standart_triangle():
    standart_triangle = Triangle(4, 5, 3)
    yield standart_triangle
    del standart_triangle


@pytest.fixture
def standart_square():
    standart_square = Square(10)
    yield standart_square
    del standart_square


@pytest.fixture
def standart_circle():
    standart_circle = Circle(5)
    yield standart_circle
    del standart_circle


@pytest.fixture
def standart_rectangle():
    standart_rectangle = Rectangle(4, 6)
    yield standart_rectangle
    del standart_rectangle
