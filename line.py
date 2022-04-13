import math

class Point:
    # def __init__(self,x1,y1,x2,y2):
    #     self.x1 = x1
    #     self.y1 = y1
    #     self.x2 = x2
    #     self.y2 = y2 
    
    # def get_x1(self):
    #     return self.x1

    # def set_x1(self, x1):
    #     try:
    #         float(x1)
    #         self.x1 = x1
    #     except ValueError:
    #         print("x-coordinate must be a numerical value.")
    
    # def set_y1(self, y1):
    #     try:
    #         float(y1)
    #         self.y1 = y1
    #     except ValueError:
    #         print("y-coordinate must be a numerical value.")

    # def get_y1(self):
    #     return self.y1

    # def set_x2(self, x2):
    #     try:
    #         float(x2)
    #         self.x2 = x2
    #     except ValueError:
    #         print("x-coordinate must be a numerical value.")

    # def get_x2(self):
    #     return self.x2
    
    # def set_y2(self, y2):
    #     try:
    #         float(y2)
    #         self.y2 = y2
    #     except ValueError:
    #         print("y-coordinate must be a numerical value.")

    # def get_y2(self):
    #     return self.y2

    def slope(x1, y1, x2, y2): 
        return (y2-y1)/(x2-x1)

    def distance(x1, y1, x2, y2):
        return (math.sqrt(((y2-y1)**2) + ((x2-x1)**2)))
