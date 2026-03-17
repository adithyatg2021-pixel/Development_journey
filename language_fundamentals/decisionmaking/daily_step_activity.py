steps = int(input("Enter number of steps:"))

if steps >= 10000:
    print("Active")
elif steps > 5000:
    print("Moderately Active")
else:
    print("Sedentary")