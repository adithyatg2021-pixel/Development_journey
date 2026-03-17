def product_of_nums(*args):
    product = 1
    for num in args:
        product *= num
    return product

print(product_of_nums(1,2,3))
print(product_of_nums(1,2,3,4))
print(product_of_nums(1,2,3,4,5))
