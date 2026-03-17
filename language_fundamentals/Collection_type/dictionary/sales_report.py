
sales_report = {
    "sun":18000,
    "mon":20000,
    "tue":15000,
    "wed":17000,
    "thu":12000,
    "fri":14000,
    "sat":19000
}

# # display day wise sales

# for key in sales_report:

#     print(f"{key}:{sales_report[key]}")

# # total sales

# total_sale = 0

# for key in sales_report:

#     total_sale += sales_report[key]

# print("Total sales:",total_sale)

# # Display average sales

# avg_sales = total_sale/len(sales_report)

# print("Average sales:",avg_sales)

# # display day where sales < avg_sales

# for key in sales_report:
#     if sales_report[key] < avg_sales:
#         print("Days with sales less than average sale:",key)

# Highest sale


highest_sale = 0
lowest_sale = sales_report["sun"]

for key in sales_report:
    if sales_report[key] > highest_sale:
        highest_sale = sales_report[key]
        highest_sale_day = key
    if sales_report[key] < lowest_sale:
        lowest_sale = sales_report[key]
        lowest_sale_day = key    
print("Day with highest sale:",highest_sale_day)
print("Day with lowest sale:",lowest_sale_day)




