# import math module for calculate sqrt
import math  

# define area class as base 
class Area():
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3 =side3
    
    # property to calculate semiperimeter
    @property    
    def semiperimeter(self):
        return ((self.side1+self.side2+self.side3)/2)

        
# define Triangle class as subclass
class Triangle(Area):
     def calculate_area(self):
         return (math.sqrt(self.semiperimeter*(self.semiperimeter-self.side1)* (self.semiperimeter-self.side2)* (self.semiperimeter-self.side3)))
        
    
triangle =Triangle(10,10,10)
triangle.calculate_area()