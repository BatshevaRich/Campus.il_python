import itertools

def mult_tuple(tuple1, tuple2):
    return list(itertools.product(tuple1, tuple2))

first_tuple = (1, 2)
second_tuple = (4, 5)
print(mult_tuple(first_tuple, second_tuple))

first_tuple = (1, 2, 3)
second_tuple = (4, 5, 6)
print(mult_tuple(first_tuple, second_tuple))