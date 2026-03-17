def mark_calculator(*args,**kwargs):
    option = kwargs.get("option")

    if option == "average":
        avg = sum(args) /len(args)
        return avg
    elif option == "total":
        return sum(args)
    elif option == "highest":
        return max(args)
    
print(mark_calculator(40,45,38,42,option = "average"))
print(mark_calculator(40,45,38,42,option = "total"))
print(mark_calculator(40,45,38,42,option = "highest"))