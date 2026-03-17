day = int(input("Enter day number:"))

match day:
    case 1:print("SUN")
    case 2:print("MON")
    case 3:print("TUE")
    case 4:print("WED")
    case 5:print("THU")
    case 6:print("FRI")
    case 7:print("SAT")
    case _:print("INVALID")