def is_greater(my_list, n):
    greater = list()
    for element in my_list:
        if element > n:
            greater.append(element)
    return greater

print(is_greater([1, 30, 25, 60, 27, 28], 28))
