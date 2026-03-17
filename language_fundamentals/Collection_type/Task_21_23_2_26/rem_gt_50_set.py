
st = {12,78,3,56,23,90,78}
rem_ele = set()

for ele in st:
    if ele > 50:
        rem_ele.add(ele)

print("Set after removing elements greater than 50:",st.difference(rem_ele))

