import unittest

class Circle:
    
    def __init__(self, radius):
        #Raise error if radius is non-numeric value
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('Radius must be a numeric value')
    
        #Raise error if radius is negative
        if radius < 0 :
            raise ValueError('Radius must be positive')
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2
               
    def circumference(self):
        return 2 * 3.14 * self.radius


        
class CircleTests(unittest.TestCase):

    def test_area(self):
        # Defining a circle c1 with positive radius and check the area
        c1 = Circle(5)
        self.assertEqual(c1.area(), 78.5)


    def test_non_numeric_radius(self):
        # Defining a circle c2 with negative radius
        # Check if it displays the error message
        with self.assertRaises(TypeError) as e:
            c = Circle("Hello")
        self.assertEqual(str(e.exception), 'Radius must be a numeric value')

    def test_negative_radius(self):
        # Defining a circle c2 with negative radius
        # Check if it displays the error message
        with self.assertRaises(ValueError) as e:
            c = Circle(-5)
        self.assertEqual(str(e.exception), 'Radius must be positive')


    def test_area_with_min_radius(self):
        # Defining a circle c1 with radius = 0 and check the area
        c1 = Circle(0)
        self.assertEqual(c1.area(), 0)
    
    
    def test_circumference(self):
        # Defining a circle with radius 4 and check the circumference
        c1 = Circle(4)
        self.assertEqual(c1.circumference(), 25.12)

    def test_circumference_with_min_radius(self):
        # Defining a circle c1 with radius = 0 and check the area
        c1 = Circle(0)
        self.assertEqual(c1.area(), 0)
    
    
if __name__ == "__main__":
    unittest.main()