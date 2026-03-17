class Bird:
    def fly(self): pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow fly")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich fly")

sparrow_inst = Sparrow()
sparrow_inst.fly()

ostrich_inst = Ostrich()
ostrich_inst.fly()

