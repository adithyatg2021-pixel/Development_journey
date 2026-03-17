"""
sets are defined using {} with one value
empty sets can be created as the object of set() class
sets are unordered 
sets are mutable
duplicates are not allowed
"""

di = {} # this will be empty dictionary

st = {10}
st1 = set() #empty set

print(st1)

st2 = {10,20,30,40,20} 

print(st2) # order of objects not followed, duplicated are not allowed 

# accessing values

for num in st2:
    print(num)

colors = {"blue","green","blue","orange"}
print(colors)

st = {True,False,0,1,"orange","yellow"}

print(st)