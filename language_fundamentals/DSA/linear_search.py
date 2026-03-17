class LinearSearch:
    def solution(self,arr,element):
        is_present = False
        for num in arr:
            if num == element:
                is_present =  True
                break
        return is_present
    
ls_instance = LinearSearch()

arr = [12,45,78,34,67,15,90]
element = int(input("Enter element to search:"))
print(ls_instance.solution(arr,element))
