class Rectangle:

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):

        print(f"Area of rectangle with length {self.length} and width {self.width}:{self.length * self.width}")

rect_instance1 = Rectangle(4,5)
rect_instance1.area()