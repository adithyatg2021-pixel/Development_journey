month = int(input("Enter month (in number)"))

match month:
    case 1:print("January")
    case 2:print("February")
    case 3:print("March")
    case 4:print("April")
    case 5:print("May")
    case 6:print("June")
    case 7:print("July")
    case 8:print("August")
    case 9:print("September")
    case 10:print("October")
    case 11:print("November")
    case 12:print("December")

# or

# match month:
#     case "jan"|"mar"|"july"|"aug"|"oct"|"dec":
#         print(31)
#     case "apr"|"june"|"sep"|"nov":
#         print(30)
#     case "feb":
#         print(28)
