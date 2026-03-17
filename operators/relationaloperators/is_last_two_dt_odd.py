
number = 1234

last_two_dt = number % 100 # 1234 % 100 = 34

print("Last two digit:",last_two_dt)

is_last_two_dt_odd = last_two_dt % 2 != 0 # 34 % 2 = 0, 0 != 0 = False

print(is_last_two_dt_odd) # False