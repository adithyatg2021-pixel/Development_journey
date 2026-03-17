
tips_data =  [
    {"total_bill": 16.99, "tip": 1.01, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 10.34, "tip": 1.66, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 3},
    {"total_bill": 21.01, "tip": 3.50, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 3},
    {"total_bill": 23.68, "tip": 3.31, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 24.59, "tip": 3.61, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 25.29, "tip": 4.71, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 8.77,  "tip": 2.00, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 26.88, "tip": 3.12, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 15.04, "tip": 1.96, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 14.78, "tip": 3.23, "sex": "Female", "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 10.27, "tip": 1.71, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 35.26, "tip": 5.00, "sex": "Female", "smoker": "Yes", "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 15.42, "tip": 1.57, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 18.43, "tip": 3.00, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 14.83, "tip": 3.02, "sex": "Female", "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 21.58, "tip": 3.92, "sex": "Male",   "smoker": "Yes", "day": "Fri",  "time": "Dinner", "size": 2},
    {"total_bill": 10.33, "tip": 1.67, "sex": "Female", "smoker": "No",  "day": "Fri",  "time": "Lunch",  "size": 2},
    {"total_bill": 16.29, "tip": 3.71, "sex": "Male",   "smoker": "Yes", "day": "Fri",  "time": "Lunch",  "size": 3},
    {"total_bill": 13.37, "tip": 2.00, "sex": "Female", "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 12.69, "tip": 2.31, "sex": "Male",   "smoker": "Yes", "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 17.92, "tip": 4.08, "sex": "Male",   "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 20.29, "tip": 2.75, "sex": "Female", "smoker": "Yes", "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 15.77, "tip": 2.23, "sex": "Male",   "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 39.42, "tip": 7.58, "sex": "Male",   "smoker": "Yes", "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 19.82, "tip": 3.18, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2}
]

# Highest bill

highest_bill = max([td.get("total_bill") for td in tips_data])
print("Highest bill:",highest_bill)

# Lowest bill

lowest_bill = min([td.get("total_bill") for td in tips_data])
print("Lowest bill:",lowest_bill)

# Total bill of that week

total_bill = [td.get("total_bill") for td in tips_data]
print("Total bill:",total_bill)

# High tip

high_tip = max([td.get("tip") for td in tips_data])
print("High tip:",high_tip)

# Number of females 

number_of_females = len([td for td in tips_data if td.get("sex") == "Female"])
print("Count of female customers:",number_of_females)

# Count of Male smoker

male_smoker_count = len([td for td in tips_data if td.get("sex") == "Male" and td.get("smoker") == "Yes"])
print("Count of male smokers:",male_smoker_count)

# Total bill of sunday

total_bill_sunday = sum([td.get("total_bill") for td in tips_data if "day" == "Sun"])

# High tip on which day

high_tip_day = [td.get("day") for td in tips_data if td.get("total_bill") == high_tip]

# Largest group size

large_group_size = max([td.get("size") for td in tips_data])

# Average total bill by day

average_total_bill_day = {td.get("day"):sum([td.get("total_bill")])/len([td.get("total_bill")]) for td in tips_data}
print("Total bill per day:",average_total_bill_day)



