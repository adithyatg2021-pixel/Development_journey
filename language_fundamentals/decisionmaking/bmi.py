h_in_cm = int(input("Enter height in cm:"))

w_in_kg = int(input("Enter weight in kilogram:"))

h_in_m  = h_in_cm / 100

bmi = w_in_kg / (h_in_m ** 2)

bmi = round(bmi)

print("BMI:",bmi)

if bmi < 20:
    print("Underweight")
elif  bmi < 25:
    print("Normal")
elif  bmi < 30:
    print("Overweight")
else:
    print("Obese")