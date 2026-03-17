def number_checker(*args,**kwargs):
    type = kwargs.get("type")
    if type == "odd":
        return len([num for num in args if num % 2 != 0])
    elif type == "even":
        return len([num for num in args if num % 2 == 0])
    elif type == "positive":
        return len([num for num in args if num > 0] )
    elif type == "negative":
        return len([num for num in args if num < 0])
    

print(number_checker(10,11,12,13,14,15,type = "odd"))
print(number_checker(10,11,12,13,14,15,16,type = "even"))
print(number_checker(10,11,12,13,14,15,16,type = "positive"))
print(number_checker(10,11,12,13,14,-15,-16,type = "negative"))
       