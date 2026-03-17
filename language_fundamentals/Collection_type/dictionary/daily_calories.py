
daily_calories = {
    "sun":1800,
    "mon":2000,
    "tue":1500,
    "wed":1700,
    "thu":1200,
    "fri":1400,
    "sat":1900
}

# iteration

for key in daily_calories:
    print(f"{key} : {daily_calories[key]}")

# total calories

total_calories = 0

for k in daily_calories:

    total_calories += daily_calories[k]

print("Total calories:",total_calories)

print("Avarage calories:",total_calories/len(daily_calories))