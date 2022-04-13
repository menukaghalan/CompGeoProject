import math

class Point:
    
    def slope(x1, y1, x2, y2): 
        return (y2-y1)/(x2-x1)

    def distance(x1, y1, x2, y2):
        return (math.sqrt(((y2-y1)**2) + ((x2-x1)**2)))
