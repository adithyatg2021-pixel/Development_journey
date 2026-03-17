
available_tables = range(4,10)

table_num = int(input("Enter table number:"))

if table_num in available_tables:
    food = input("Enter food availability:")

    if food == "yes":
        print("Order placed")
    else:
        print("Item out of stock")
else:
    "Invalid table number"

