"""
class list:

    def append(self,object) => add object end of the list

    def insert(self,index,object) => add object to the specified index

    def pop(self,index=-1) => remove and return specified element at index

    def remove(self,remove) => remove first occurance of object

    def count(self,object) => returns the number of occurance of specified object 

    def copy(self) => to copy the list to another variable

    def sort(self,reverse = False) => sort the list in ascending order in default

    def reverse(self) => to reverse the list

    def extend(self,iterable) => extend the list with new list

    def clear(self) => empty the list
"""

# colours = ["red","blue","green"]

#           0       1       2

# colours.append("black")

# print(colours)

#------------------------------------------

# colours.insert(1,"yellow")

# print(colours)          #[r,y,b,g] 


#-----------------------------------------

# removed_element = colours.pop(1)

# print(colours) # [r,g]


# colours.pop()             
# print(colours)  # [r,b]

#---------------------------------------

# colours.remove("blue")

# print(colours)

#--------------------------------------

# color = ["red","green","blue","red","yellow","red"]

# print(color.count("red"))

#--------------------------------------------

#aks_colo = ["red","green","yellow"]

# sre_colo = aks_colo # both the variables are pointing to same memory location. Therefor the changes
#                     # applied to anyone of the variable affect both variable

# print(aks_colo is sre_colo) # is identity operator checks whether 2 variables are pointing same memory
#                             # or not

# print(aks_colo == sre_colo) # comparing values


# sre_colo = aks_colo.copy()

# print(aks_colo is sre_colo) # False, both the variables are pointing to different memory locations.

# print(aks_colo == sre_colo)  # values in both lists are same

#-------------------------------------------------------------------

# numbers = [2,5,1,8,4,5,6]

# numbers.sort()

# print(numbers)

# numbers.sort(reverse=True)

# print(numbers)

#----------------------------------------------------

color = ["red","green","blue","red","yellow","red"]

# color.sort() 

# print(color)

# color.sort(reverse=True)

# print(color)

# color.reverse()

# print(color)

#-----------------------------------------------------

# new_color = ["brown","black"]

# # color.append(new_color)

# # print(color)

# color.extend(new_color)

# print(color)

#----------------------------------------------

color.clear()

print(color)