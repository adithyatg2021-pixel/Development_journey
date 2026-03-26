from copy import copy

class Shallow:
    def name(self):
        print("Adithya")

name_inst = Shallow()
name_inst1 = copy(name_inst)

name_inst.name()
name_inst1.name()

