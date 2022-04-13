import unittest
from line import Point

# line_obj = Point(5, 8, 3, 4)
# print("Slope of the points is = ", line_obj.slope())
# print("Distance between the two points is = ", line_obj.distance())

class TestLine(unittest.TestCase):
    def test_slope(self):
        result = Point.slope(5,8,3,4)
        self.assertEqual(result, 2)

    def test_distance(self):
        result = Point.distance(5,8,3,4)
        self.assertEqual(result, 4.47213595499958)

    def test_distance(self):
        result = Point.distance(5,8,3,4)
        self.assertNotEqual(result, "hello")

# def test_init_():
#     P = Point(5,8,3,4)
#     assert isinstance(P, Point)

# def test_get_x1():
#     x1 = line_obj.x1
#     x1_2 = line_obj.get_x1()

#     assert x1 == x1_2

# def test_set_x1():
#     line_obj.set_x1(5)
#     assert line_obj.x1 == 5

#     # line_obj.set_x1("hehe")
#     # assert line_obj.x1 == 5


