import pytest


def test_name(standart_rectangle):
    assert standart_rectangle.name == 'Rectangle'


def test_perimeter(standart_rectangle):
    assert standart_rectangle.perimeter == 20


def test_area(standart_rectangle):
    assert standart_rectangle.area == 24


def test_add_area_square(standart_rectangle, standart_triangle):
    assert standart_rectangle.add_area(standart_triangle) == 30


def test_add_area_rectangle(standart_rectangle, standart_square):
    assert standart_rectangle.add_area(standart_square) == 124


def test_add_area_circle(standart_rectangle, standart_circle):
    assert standart_rectangle.add_area(standart_circle) == 102.54


def test_add_area_not_a_figure(standart_rectangle):
    with pytest.raises(ValueError):
        standart_rectangle.add_area(1)
