
rating = float(input("Enter rating:")) # 4.3

if rating < 4.0: # 4.3 < 4.0 [F]
    print("Unsatisfied")
elif rating >= 4.0 and rating < 4.5: # 4.3 > 4.0 [T] and 4.3 < 4.5 [T] => True
    print("Neutral")
else:
    print("Satisfied")