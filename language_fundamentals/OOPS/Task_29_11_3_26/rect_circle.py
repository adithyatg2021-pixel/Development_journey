class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print("Area of rectangle:",self.l * self.b)

class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        print("Area of circle:",3.14 * self.r * self.r)

rect_instance = Rectangle(5,6)
rect_instance.area()
circle_instance = Circle(5)
circle_instance.area()