num = int(input("Enter number:"))

if num == 0:
    sign = "Zero number"
elif num > 0:
    sign = "Positive number"
else:
    sign = "Negative number"

match sign:
    case "Zero number":print("Zero number")
    case "Positive number":print("Positive number")
    case "Negative number":print("Negative number")


# or

# match num:
#     case 0:print("Zero")
#     case _ if num>0:print("+ve")
#     case _ if num<0:print("-ve")
#     casw _:print("invalid")