
"""
class dict:

    def keys(self) => return all keys

    def values(self) => return all values 

    def items(self) => return keys and values

    def get(self,key) => return the value of specified key

    def pop(self,key) => remove the key value pair based on the specified key
"""

employee = {"id":789,"name":"Hari","Salary":23000,"Dept":"qa"}

# print("All keys from employee dict:")

# for key in employee.keys():
#     print(key)

# print("\n")

# print("All values from employee dict:")

# for val in employee.values():
#     print(val)

# print("All keys and values from employee dict:")

# for k,v in employee.items():
#     print(k,v)


print(employee["name"]) # Hari

print(employee.get("name")) # Hari

"""
these both methods are used to return values using keys. 
In the case of first method if the key doesn't exist then it will raise an error
Instead of using get method can return "None" as the output for not existing key 
"""

print(employee.get("email","dummy@gmail.com"))

"""
In this case key - email is not existing. Then the method will return "dummy@gmail.com" (second parameter)
as the output instead of raising an error.
"""

print(employee.pop("Dept")) #qa

print(employee)