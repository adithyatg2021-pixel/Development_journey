
fr = open("language_fundamentals\\Collection_type\\Files\\food_logs.txt")

food_logs = []      #convert text data which is in string form to list of dictionaries
for line in fr:      
    data = line.rstrip("\n").split(",")  #1,break_fast,idly,175,11-1-2025,hari

    food_dict = {"id":data[0],"meal_type":data[1],"name":data[2],"calorie":data[3],"date":data[4],"owner":data[5]}
    food_logs.append(food_dict)
print(food_logs)       #print outside for loop