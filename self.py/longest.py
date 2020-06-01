def longest(my_list):
    return max(my_list, key=lambda x:len(x))

print(longest(["111", "234", "2000", "goru", "birthday", "09"]))