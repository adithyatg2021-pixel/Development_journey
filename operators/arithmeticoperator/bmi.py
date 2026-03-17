"""
Program to calculate bmi
BMI = weight in kilogram / (height in meter ^ 2)
"""

h_in_cm = 177 # h_in_cm  = 177
w_in_kg = 65 # w_in_kg = 65
h_in_m = h_in_cm / 100 #h_in_m = 1.77 = 177/100 = h_in_m / 100 
bmi = w_in_kg / (h_in_m ** 2) # bmi = 65/(1.77 ^ 2) = w_in_kg/(h_in_m **2)
print("BMI:",bmi) # BMI: bmi