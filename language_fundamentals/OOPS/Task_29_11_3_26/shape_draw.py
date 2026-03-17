class Shape:
    def draw(self): pass

class Square(Shape):
    def draw(self):
        print("Draw square")

class Triangle(Shape):
    def draw(self):
        print("Draw triangle")

square_inst = Square()
square_inst.draw()

triangle_inst = Triangle()
triangle_inst.draw()
