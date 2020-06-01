def chocolate_maker(small, big, x):
    if (small + big * 5) >= x:
        return True
    return False

print(chocolate_maker(3, 1, 8))
print(chocolate_maker(3, 1, 9))
print(chocolate_maker(3, 2, 10))
