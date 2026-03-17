class Mobile():

    def __init__(self,image,name,price,rating):
        self.image = image
        self.name = name
        self.price = price
        self.rating = rating

    def display(self):
        print("Mobile details:")
        print("Image:",self.image)
        print("Name:",self.name)
        print("Price:",self.price)
        print("Rating:",self.rating)
        print("\n")

mobile_instance1 = Mobile("Iphone16.jpg","iphone16",150000,5)
mobile_instance1.display()

mobile_instance2 = Mobile("Galaxy.jpg","Samsung Galaxy A21S",50000,4.5)
mobile_instance2.display()