def shift_left(my_list):
    return my_list[1:] + my_list[:1]

print(shift_left([0, 1, 2]))
print(shift_left(['monkey', 2.0, 1]))