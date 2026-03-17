heart_rate = int(input("Enter heart rate (beats per minute):"))

if heart_rate < 60:
    print("Low heart rate")
elif heart_rate <= 100:
    print("Normal heart rate")
else:
    print("Hight heart rate")