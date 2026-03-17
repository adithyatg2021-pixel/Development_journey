class Circle:

    def __init__(self,radius):
        self.radius = radius
    def display(self):
        print(f"Area of circle with radius {self.radius}: {3.14 * self.radius * self.radius}")

circle1 = Circle(6)
circle1.display()