is_loc_phat = lambda x: set(str(x)).issubset({'6', '8'})
loc_phat_numbers = [x for x in range(1000) if is_loc_phat(x)]
print(loc_phat_numbers)