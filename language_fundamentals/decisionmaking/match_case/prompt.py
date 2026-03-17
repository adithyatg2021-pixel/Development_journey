
prompt = input("Enter prompt:")

match prompt:
    case "start":print("System starting....")

    case "stop":print("System stoping xxxx")

    case "restart":print("System restarting !!!!")

    case _:print("Invalid prompt...")