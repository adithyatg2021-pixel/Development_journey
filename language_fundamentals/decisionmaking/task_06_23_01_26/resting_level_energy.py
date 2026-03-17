energy_score = int(input("Enter energy score (1-10)"))

if energy_score >= 1 and energy_score < 4:
    print("Low energy")
elif energy_score >= 4 and energy_score < 8:
    print("Moderate energy")
else:
    print("High energy")
