
"""
products = [
    [1, "iPhone 15", "Apple", "Electronics", 79999, 120],
    [2, "Galaxy S24", "Samsung", "Electronics", 74999, 150],
    [3, "MacBook Air M2", "Apple", "Electronics", 114999, 80],
    [4, "Air Jordan Shoes", "Nike", "Footwear", 12999, 200],
    [5, "Noise Smartwatch", "Noise", "Accessories", 2999, 300],
    [6, "HP Pavilion Laptop", "HP", "Electronics", 65000, 60],
    [7, "Levi's Jeans", "Levi's", "Clothing", 2499, 250],
    [8, "Boat Rockerz 450", "Boat", "Accessories", 1499, 500]
]

1. display all product names
2. product with the highest price
3. display electronics products
4. display products where the brand is Apple
5. which category has most products
6. product with maximum stock
7. list all categories
"""
products = [
    [1, "iPhone 15", "Apple", "Electronics", 79999, 120],
    [2, "Galaxy S24", "Samsung", "Electronics", 74999, 150],
    [3, "MacBook Air M2", "Apple", "Electronics", 114999, 80],
    [4, "Air Jordan Shoes", "Nike", "Footwear", 12999, 200],
    [5, "Noise Smartwatch", "Noise", "Accessories", 2999, 300],
    [6, "HP Pavilion Laptop", "HP", "Electronics", 65000, 60],
    [7, "Levi's Jeans", "Levi's", "Clothing", 2499, 250],
    [8, "Boat Rockerz 450", "Boat", "Accessories", 1499, 500]
]

# all product names

product_names= [lst[1] for lst in products]
print(product_names)

# product with the highest price

highest_price = max([lst[4] for lst in products])
product_high_price = [lst[1] for lst in products if lst[4] == highest_price]
print("Product with highest price:",product_high_price)

# display electronics products
electronic_prod = [lst[1] for lst in products if lst[3] == "Electronics"]
print("Electronic products:",electronic_prod)

# display products where the brand is Apple

product_brand = [lst[1] for lst in products if lst[2] == "Apple"]
print("Name of products with brand Apple:",product_brand)

#  which category has most products

category = [lst[3] for lst in products]
category_count = {cat:category.count(cat) for cat in category}

# maximum = 0
# for k,v in category_count.items():
#     if v > maximum:
#         maximum = v
#         key = k
# print("Category with maximum products:",key)

category_count_lst = [[v,k] for k,v in category_count.items()]
sorted_cat_count_lst = sorted(category_count_lst,reverse=True)
print("Category has most products:",sorted_cat_count_lst[0][1])

# product with maximum stock

max_stock = max([lst[-1] for lst in products])
product_with_max_stock = [lst[1] for lst in products if lst[-1] == max_stock]
print("Product with maximum stock:",product_with_max_stock)

# list all categories

categories = {lst[3] for lst in products}
categories = list(categories)
print("List of product categories:",categories)