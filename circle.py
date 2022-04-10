class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self): 
        return self.radius 
      
    def set_radius(self, radius): 
        self.radius = radius
    
    def area(self):
        return self.radius**2*3.14
    
    def perimeter(self):
        return 2*self.radius*3.14
