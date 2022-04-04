import pytest
from point import Point


@pytest.fixture
def my_point() -> Point:
    return Point(1, 2)


def test_point(my_point):
    assert isinstance(my_point, Point)


def test_set_x(my_point):
    x = 3
    my_point.set_x(x)
    assert my_point.x == x

    my_point.set_x("fish")
    assert my_point.x == x


def test_get_x(my_point):
    assert my_point.x == my_point.get_x()


def test_set_y(my_point):
    y = 3
    my_point.set_y(y)
    assert my_point.y == y

    my_point.set_y("fish")
    assert my_point.y == y


def test_get_y(my_point):
    assert my_point.y == my_point.get_y()
