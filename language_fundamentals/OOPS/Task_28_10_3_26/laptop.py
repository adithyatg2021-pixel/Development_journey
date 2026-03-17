class Laptop:
    def __init__(self,brand,RAM):
        self.brand = brand
        self.ram = RAM

    def display(self):
        print("Laptop specifications:")
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram}")

laptop1 = Laptop("Dell 15 laptop", "8 GB")
laptop1.display()