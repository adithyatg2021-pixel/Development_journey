def calculator(*args,**kwargs):

    if kwargs.get("key") == "+":
        return sum(args)
    if kwargs.get("key") == "*":
        p = 1
        for num in args:
            p *= num
        return p
    if kwargs.get("key") == "-":
        num1 = args[0]
        num2 = args[1]
        return num1 - num2 if num1 > num2 else num2 - num1
    
print(calculator(10,20,30,key = "+"))
print(calculator(10,20,30,key = "*"))
print(calculator(30,15,key = "-"))

