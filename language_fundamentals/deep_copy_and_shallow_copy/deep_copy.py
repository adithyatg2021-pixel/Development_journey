"""
shallow copy: creating copy of outer object
deep copy: creating copy of inner object
"""
from copy import deepcopy

arun_fvt_foods =[
    {"meal_type":"breakfast","meal":"dosa"},
    {"meal_type":"lunch","meal":"meal"},
    {"meal_type":"dinner","meal":"fried rice"}
]

# hari_fvt_foods = arun_fvt_foods.copy()
# hari_fvt_foods[0]["meal"] = "idly"

# print("Arun",arun_fvt_foods)
# print("Hari",hari_fvt_foods)

hari_fvt_foods=deepcopy(arun_fvt_foods)
hari_fvt_foods[0]["meal"] = "idly"

print("Arun",arun_fvt_foods)
print("Hari",hari_fvt_foods)

