import pytest

def test_name(standart_square):
    assert standart_square.name == 'Square'


def test_perimeter(standart_square):
    assert standart_square.perimeter == 40


def test_area(standart_square):
    assert standart_square.area == 100


def test_add_area_square(standart_square, standart_triangle):
    assert standart_square.add_area(standart_triangle) == 106


def test_add_area_rectangle(standart_square, standart_rectangle):
    assert standart_square.add_area(standart_rectangle) == 124


def test_add_area_circle(standart_square, standart_circle):
    assert standart_square.add_area(standart_circle) == 178.54


def test_add_area_not_a_figure(standart_square):
    with pytest.raises(ValueError):
        standart_square.add_area(int)
