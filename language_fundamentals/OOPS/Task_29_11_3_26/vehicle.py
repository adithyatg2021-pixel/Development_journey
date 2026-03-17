class Vehicle:
    def move(self): pass

class Car(Vehicle):
    def move(self):
        print("Car mmoves")

class Airplane(Vehicle):
    def move(self):
        print("Airplane fly")

car_inst = Car()
car_inst.move()

airplane_inst = Airplane()
airplane_inst.move()