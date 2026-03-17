class Animal:
    def eat(self): pass

class Lion(Animal):
    def eat(self):
        print("Lion eats")

class Cow(Animal):
    def eat(self):
        print("Cow eats")

lion_inst = Lion()
lion_inst.eat()

cow_inst = Cow()
cow_inst.eat()