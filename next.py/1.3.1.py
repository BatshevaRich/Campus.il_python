def intersection(list_1, list_2):
    return list(set([x for x in list_1 for y in list_2 if x == y if x]))

print(intersection([1, 2, 3, 4], [8, 3, 9]))
print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
