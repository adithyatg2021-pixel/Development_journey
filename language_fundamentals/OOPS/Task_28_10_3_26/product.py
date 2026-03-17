class Product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def display(self):
        print(f"Product name: {self.name}")
        print(f"Price: {self.price}")

product1 = Product("Tooth paste",100)
product1.display()