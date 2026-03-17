def analyze_number(*args,**kwargs):
    action = kwargs.get("action")

    if action == "max":
        return max(args)
    if action == "min":
        return min(args)
    if action == "count":
        return len(args)
print(analyze_number(10,11,12,13,14,15,action = "max"))
print(analyze_number(10,11,12,13,14,15,action = "min"))
print(analyze_number(10,11,12,13,14,15,action = "count"))