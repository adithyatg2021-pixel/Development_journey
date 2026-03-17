
element = int(input("Enter the element to search:"))

tup = (34,78,90,23,67)

if element in tup:
    print(element,"is in tuple")
else:
    print(element,"not in tuple")