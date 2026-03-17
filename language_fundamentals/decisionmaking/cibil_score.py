cibil_score = int(input("Enter CIBIL Score:"))

if cibil_score >= 300 and cibil_score < 550:
    print("POOR")
elif cibil_score >= 550 and cibil_score < 650:
    print("AVERAGE")
elif cibil_score >= 650 and cibil_score < 750:
    print("GOOD")
elif cibil_score >= 750 and cibil_score <= 900:
    print("EXCELLENT")