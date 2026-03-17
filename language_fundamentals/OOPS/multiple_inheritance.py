"""
Inheriting the features of multiple classes
"""

class Father:
    def coaching_skill(self):
        print("Coaching skill")

class Mother:
    def cooking_skill(self):
        print("Cooking skill")

class Child(Father,Mother): # multiple inheritance , inheriting the features of parent classes based on the order of inheritance
    pass

child_instance = Child()
child_instance.coaching_skill()
child_instance.cooking_skill()