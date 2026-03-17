
print("List before removing duplicate elements:")
lis = [23,56,23,44,78,23,56,78]

print(lis)

st = set()

for ele in lis:
    st.add(ele)

lis = list(st)

print("New list:",lis)

