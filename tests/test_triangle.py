import pytest
from src.Triangle import Triangle


def test_name(standart_triangle):
    assert standart_triangle.name == 'Triangle'


def test_perimeter(standart_triangle):
    assert standart_triangle.perimeter == 12


def test_area(standart_triangle):
    assert standart_triangle.area == 6


def test_add_area_square(standart_triangle, standart_square):
    assert standart_triangle.add_area(standart_square) == 106


def test_add_area_rectangle(standart_triangle, standart_rectangle):
    assert standart_triangle.add_area(standart_rectangle) == 30


def test_add_area_circle(standart_triangle, standart_circle):
    assert standart_triangle.add_area(standart_circle) == 84.54


@pytest.mark.parametrize('side_tuple', [
    (4, 5, 3, 3),
    (4, 5),
    (),
    (4, 5, 230),
    (4, 5, 0)

])
def test_value_error_wrong_sides(side_tuple):
    with pytest.raises(ValueError):
        wrong_triangle = Triangle(*side_tuple)


def test_add_area_not_a_figure(standart_triangle):
    with pytest.raises(ValueError):
        standart_triangle.add_area(None)
