class Shape:
    def area(self):
        print("Finding area of shape.")

class Square(Shape):    # Inheriting class Shape
    def __init__(self,side):
        self.s = side
    def area(self): # overriding the method area which predefined in class Shape
        print("Area of square:",self.s ** 2)

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print("Area of rectangle:",self.l * self.b)

class Triangle(Shape):
    def __init__(self,b,h):
        self.b = b
        self.h = h
    def area(self):
        print("Area of triangle:",0.5 * self.b * self.h)

square_instance = Square(5)
square_instance.area()

rectangle_instance = Rectangle(3,4)
rectangle_instance.area()

triangle_instance = Triangle(7,4)
triangle_instance.area()