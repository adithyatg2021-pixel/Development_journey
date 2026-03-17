
fr = open("language_fundamentals\\Collection_type\\Files\\flight.txt")

flight_details = []

for line in fr:
    data = line.rstrip("\n").split(",")
    flight = {"year":data[0],"Month":data[1],"Passenger_count":int(data[2])}
    flight_details.append(flight)

year_wise_pass_count = {}

for f in flight_details:
    year = f.get("year")
    p_count = f.get("Passenger_count")
    if year in year_wise_pass_count:
        year_wise_pass_count[year] += p_count
    else:
        year_wise_pass_count[year] = p_count
print(year_wise_pass_count)

year_wise_pass_count_sorted_lst = sorted([[v,k] for k,v in year_wise_pass_count.items()])
print(year_wise_pass_count_sorted_lst)

# or

year_pass_count_sorted = sorted(year_wise_pass_count,key=year_wise_pass_count.get,reverse=True)
print(year_pass_count_sorted)