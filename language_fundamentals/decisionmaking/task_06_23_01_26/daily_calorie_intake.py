calories = int(input("Enter calories:"))

if calories > 2500:
    print("Excess intake")
elif calories > 1500:
    print("Balanced intake")
else:
    print("Low intake")