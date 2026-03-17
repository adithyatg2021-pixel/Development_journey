screen_hours = int(input("Enter screen hours:"))

if screen_hours > 5:
    print("Excessive usage")
elif screen_hours >= 2:
    print("Moderate usage")
else:
    print("Healthy usage")
