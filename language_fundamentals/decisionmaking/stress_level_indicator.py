stress_score = int(input("Enter the stress score:"))

if stress_score > 7 and stress_score <=10:
    print("High stress")
elif stress_score > 4 and stress_score <=7:
    print("Moderate stress")
elif stress_score > 1 and stress_score <= 3:
    print("Low stress")