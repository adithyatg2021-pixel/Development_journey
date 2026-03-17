
orders = {"tea":15,"coffee":21,"dosa":34,"rice":67}

order_list = [[v,k] for k,v in orders.items()]

print("Sorted orders list:",sorted(order_list,reverse=True))

# Sorted orders list: [[67, 'rice'], [34, 'dosa'], [21, 'coffee'], [15, 'tea']]