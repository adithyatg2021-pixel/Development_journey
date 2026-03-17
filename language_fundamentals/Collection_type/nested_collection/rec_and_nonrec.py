
# list1 = ["listen","earth","moon","dad","madam","race"]
# list2 = ["silent","angel","heart","test","dam","care"]

word = "racecarfast"

# print non recursive character
# print recursive character whose count > 2

non_recursive = [ch for ch in word if word.count(ch) == 1]
print("List of non recursive characters:",non_recursive)

rec_ch_count_gt_2 = {ch:word.count(ch) for ch in word if word.count(ch) > 2}
print("List of recursive characters whose count greater than 2:",rec_ch_count_gt_2)