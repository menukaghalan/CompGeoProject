class Point:
    """a class to represent a 2-d point"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        try:
            float(x)
            self.x = x
        except ValueError:
            print("x-coordinate must be a numerical value.")

    def get_x(self):
        return self.x

    def set_y(self, y):
        try:
            float(y)
            self.y = y
        except ValueError:
            print("y-coordinate must be a numerical value.")

    def get_y(self):
        return self.y

