number = 127

last_2_digit = number % 100 # 127 % 100 = 27

is_in_range = last_2_digit >= 10 and last_2_digit <= 50 # 27 >= 10 and 27 <= 50
                                                        # True and True
print(is_in_range)