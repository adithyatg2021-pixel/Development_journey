lst = [(3,6),(4,2),(7,1),(5,9)]

sorted_data = lambda ls:sorted([(t[1],t[0]) for t in ls ])
print(sorted_data(lst))

lst.sort(key = lambda t:t[1])   # key parameter is used to customise sorting. Otherwise, it will sort based on first value
print(lst)

# or

print(sorted(lst,key=lambda t:t[1],reverse=True)) # sorting the data in desc order based on the second element of tuple 
                                                    # t[1] = second element of tuple
                                                
print(max(lst,key=lambda t:t[1]))


