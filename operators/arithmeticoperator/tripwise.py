"""
w.a.p to find the individual split of the bill amount with 8% gst for head count = 5
"""
head_count = 5

bill_amount = 237

# 8% gst
gst = 8

bill_amount += (gst / 100) * bill_amount

individual_split = bill_amount / head_count

print("Individual split:",individual_split)