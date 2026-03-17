
fr = open("language_fundamentals\\Collection_type\\Files\\orders.txt","r")


order_list = [line.rstrip("\n") for line in fr]

# Orders with count in dict
order_count = {o:order_list.count(o) for o in order_list}
print(order_count)

# Max count order

count_order_list = [[v,k] for k,v in order_count.items()]
print(count_order_list)
count_order_list.sort(reverse=True)
print("Max order item:",count_order_list)