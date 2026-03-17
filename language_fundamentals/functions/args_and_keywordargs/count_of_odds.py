def count_of_odds(*args:tuple):
    odds = [num for num in args if num % 2 != 0]
    return len(odds)

print(count_of_odds(10,11,12,13))
print(count_of_odds(10,11,12,13,14,15))