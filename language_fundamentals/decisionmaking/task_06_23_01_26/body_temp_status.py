body_temp = int(input("Enter body temperature (C):"))

if body_temp > 37.5:
    print("Fever")
elif body_temp >= 36:
    print("Normal temperature")
elif body_temp < 36:
    print("Low body temperature")