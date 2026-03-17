def count_of_evens(*args):
    # count = 0
    # for num in args:
    #     if num % 2 == 0:
    #         count += 1
    # return count

    evens = [num for num in args if num % 2 == 0]
    return len(evens)

print(count_of_evens(10,11,12,13))
print(count_of_evens(10,11,12,13,14,15,16))