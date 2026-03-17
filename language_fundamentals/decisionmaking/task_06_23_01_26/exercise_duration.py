exercise_duration = int(input("Enter exersice duration(in minutes):"))

if exercise_duration > 60:
    print("Intense Exercise")
elif exercise_duration >= 30:
    print("Good Exercise")
else:
    print("Insufficient Exercise")