
"""
class set:
    def add(self,value) => to add a value to the set. Order is not considered.

    def union(self,set) => return the union of 2 sets

    def intersection(self,set) => returns the common element from 2 sets

    def difference(self,set) => returns the elements from set_a which are not in set_b

    def issuperset(self,set) => returns True whether the set_a is the superset of set_b

    def issubset(self,set) => returns True whether the set_a is the subset of set_b
"""

foods = {"tea","coffee","dosa","cb"}

foods.add("meals")

print(foods)

#---------------------------------------

set_a = {10,20,30,40,50}

set_b = {40,50,100,200}

u_set = set_a.union(set_b)

print(u_set)    #{10,20,30,40,50,100,200} -> not ordered

i_set = set_a.intersection(set_b)

print(i_set)    #{40,50} -> not ordered

d_set = set_a.difference(set_b)

print(d_set)    #{10,20,30} -> not ordered

#---------------------------------------------

sup_set = {10,20,30,40}

sub_set = {20,40}

print(sup_set.issuperset(sub_set))  #True

print(sub_set.issubset(sup_set))    #True


