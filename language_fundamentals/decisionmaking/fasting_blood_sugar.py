fastingbloodsugar = int(input("Enter fastingBloodSugar:"))

if fastingbloodsugar < 100:
    print("Normal")
elif fastingbloodsugar < 125:
    print("Prediabets")
else:
    print("Diabets")