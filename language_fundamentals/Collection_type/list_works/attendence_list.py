
"""
H => Holiday
P => Present
"""

attendence = ['H','P','P','P','P','P','H','H','P']

#              0   1   2   3   4   5   6   7   8

# print(attendence)

attendence[4] = 'H'

# for at in attendence:
#     print(at)


holiday_count = 0
present_count = 0
leave_count = 0

for att in attendence:
    if att == 'H':
        holiday_count += 1
    elif att == 'P':
        present_count += 1
    else:
        leave_count += 1

print("Holiday count:",holiday_count)
print("Present count:",present_count)
print("Leave count:",leave_count)