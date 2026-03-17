# Attributes -> instance variable
# All class have methods to initialize attributes. For that we use constructor

class Biriyni:
    name:str
    category:str
    price:int

    def __init__(self,biriyani_name,category,price): # this method is used for initialize attributes
        self.name = biriyani_name
        self.category = category
        self.price = price

    def display(self):
        print(f"Biriyani:{self.name}")
        print(f"Category:{self.category}")
        print(f"Price:{self.price}")
        print("\n")

biriyani_1 = Biriyni("Veg biriyani","Veg",150)
biriyani_1.display()

biriyani_2 = Biriyni("CB","Non-veg",200)
biriyani_2.display()

biriyani_3 = Biriyni("Fish biriyani","Non-veg",180)
biriyani_3.display()