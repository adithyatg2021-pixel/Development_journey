
nums = [10,11,10,11,12,13,14,15,16,15]

# create a collection that contains recursive numbers

new_collection = {num for num in nums if nums.count(num) > 1}
print(new_collection)