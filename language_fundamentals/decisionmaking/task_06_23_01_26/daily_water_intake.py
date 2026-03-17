water_intake = int(input("Enter daily water intake (in liter):"))

if water_intake > 3:
    print("Excess intake")
elif water_intake >= 2:
    print("Adequate intake")
else:
    print("Dehydrated")
    