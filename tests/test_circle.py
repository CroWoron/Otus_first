import pytest


def test_name(standart_circle):
    assert standart_circle.name == 'Circle'


def test_perimeter(standart_circle):
    assert standart_circle.perimeter == 31.42


def test_area(standart_circle):
    assert standart_circle.area == 78.54


def test_add_area_square(standart_circle, standart_triangle):
    assert standart_circle.add_area(standart_triangle) == 84.54


def test_add_area_rectangle(standart_circle, standart_rectangle):
    assert standart_circle.add_area(standart_rectangle) == 102.54


def test_add_area_circle(standart_circle, standart_square):
    assert standart_circle.add_area(standart_square) == 178.54


def test_add_area_not_a_figure(standart_circle):
    with pytest.raises(ValueError):
        standart_circle.add_area(str)
