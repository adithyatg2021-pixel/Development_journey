from csv import DictReader

fr = open("language_fundamentals\\Collection_type\\Files\\tips.csv")

data = list(DictReader(fr))

# Day and tips

day_tips = {}

for t in data:
    day = t.get("day")
    tip = float(t.get("tip"))

    if day in day_tips:
        day_tips[day] += tip
    else:
        day_tips[day] = tip
print(day_tips)

# day with highest revenue

day_revenue = {}

for d in data:
    day = d.get("day")
    t_bill = float(d.get("total_bill"))

    if day in day_revenue:
        day_revenue[day] += t_bill
    else:
        day_revenue[day] = t_bill

day_t_bill_list = max([[v,k] for k,v in day_revenue.items()])
print(day_t_bill_list)

# male and female tip

male_tip = 0
female_tip = 0

for da in data:
    if da.get("sex") == "Male":
        male_tip += float(da.get("tip"))
    else:
        female_tip += float(da.get("tip"))
if male_tip > female_tip:
    print("More tips from male:",male_tip)
else:
    print("More tips from female:",female_tip)


