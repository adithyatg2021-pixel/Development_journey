
products = ["Paste","Soap","Washing power","Detol"]

prices = [50,25,200,30]

product_dict = {}

for i in range(0,len(products)):
    product_dict[products[i]] = prices[i]

print(product_dict)
