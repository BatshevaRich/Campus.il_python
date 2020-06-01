def are_lists_equal(list1, list2):
    if sorted(list1) == sorted(list2):
        return True
    return False
print(are_lists_equal([0.6, 1, 2, 3], [3, 2, 0.6, 1]))
print(are_lists_equal([0.6, 1, 2, 3], [9, 0, 5, 10.5]))
