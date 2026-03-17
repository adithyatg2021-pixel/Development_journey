
"""
create a dictionary of product with attribute id, title, price, avl_qty

"""

product_dict = {"id":128,"title":"Lux","price":25,"avl_qty":40}

print(product_dict["title"])

product_dict["avl_qty"] += 10   # {"id":128,"title":"Lux","price":25,"avl_qty":50}

print(product_dict)

# adding new key:value

product_dict["code"] = "sku12"     

print(product_dict)

# check key existing in dict

if "offer" in product_dict:
    print("Key exists.")

else:
    print("Key is not exists.")
