oxygen_level = int(input("Enter oxygen level:"))

if oxygen_level >= 95:
    print("Normal")
elif oxygen_level >= 90:
    print("Mild Concern")
else:
    print("Critical")
    