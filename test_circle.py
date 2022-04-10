import pytest
from circle import Circle

circle_obj = Circle(10)

print(circle_obj.area())
print(circle_obj.perimeter())



def test__init_():
    c = Circle(3.5)
    assert isinstance(c, Circle)


def test_get_radius():
    r = circle_obj.radius
    r2 = circle_obj.get_radius()

    assert r == r2


def test_set_radius():

    circle_obj.set_radius(5)
    assert circle_obj.radius == 5

    circle_obj.set_radius("hello")
    assert circle_obj.radius == "hello"


def test_area():
    circle_obj.set_radius(6)
    assert circle_obj.area() == 3.14*6**2


def test_perimeter():
    circle_obj.set_radius(8)
    assert circle_obj.perimeter() == 2*3.14*8

