systolic_bp = int(input("Enter systoloic pressure:"))

if systolic_bp < 120:
    print("Normal")
elif systolic_bp <= 129:
    print("Elevated")
elif systolic_bp <= 139:
    print("High BP stage1")
else:
    print("High BP stage 2")
