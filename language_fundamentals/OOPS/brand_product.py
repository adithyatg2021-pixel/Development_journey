class Brand:
    def __init__(self,name):
        self.brand_name = name
    def display(self):
        print("Brand name:",self.brand_name)

class Product(Brand):
    def set_product(self,pname,bname):
        super().__init__(bname)
        self.product_name = pname

    def display(self):
        super().display()
        print("Product name:",self.product_name)

product1 = Product("Soft drink","Coca-cola")
product1.display()
product2 = Product("Soap","Vivel")
product2.display()