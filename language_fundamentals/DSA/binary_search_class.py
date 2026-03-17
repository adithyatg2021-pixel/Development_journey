class BinarySearch:
    
    def solution(self,arr,element):
        is_present = False
        low = 0
        upp = len(arr) - 1
        arr.sort()
        while(low <= upp):
            mid = (low + upp) // 2

            if arr[mid] == element:
                is_present = True
                break
            elif element < arr[mid]:
                upp = mid - 1
            elif element > arr[mid]:
                low = mid + 1

        return is_present

bs_instance = BinarySearch()
arr = [34,90,1,7,56,34,16,79,5,45]
element = int(input("Enter element to search:"))
print(bs_instance.solution(arr,element))
