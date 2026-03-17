dictionary = {"name":"ammu","age":23,"qualification":"msc cs"}

for k in dictionary.keys():
    print(k)

print(dictionary.get("name"))
print(dictionary.pop("qualification"))
print(dictionary)