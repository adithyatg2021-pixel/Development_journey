class Shape:

    def area(self,*args):

        if len(args) == 1:
            r = args[0]

            print("Area of circle:",3.14 * r * r)

        elif len(args) == 2:
            l = args[0]
            b = args[1]

            print("Area of rectangle:",l * b)

        elif len(args) == 3:
            l = args[0]
            b = args[1]
            h = args[2]

            print("Area of cuboid:",l * b * h)

shape_inst = Shape()
shape_inst.area(5)
shape_inst.area(10,4)
shape_inst.area(3,4,5)