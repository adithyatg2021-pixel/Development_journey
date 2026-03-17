hours_of_sleep = int(input("Enter hours of sleep:"))
if hours_of_sleep > 8:
    print("Oversleeping")
elif hours_of_sleep >= 6:
    print("Healthy sleep")
else:
    print("Sleep deprived")