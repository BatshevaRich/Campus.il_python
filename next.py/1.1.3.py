def divided_by_four(a):
    return a % 4 == 0

def four_dividers(number):
    return list(filter(divided_by_four, range(1, number)))

print(four_dividers(9))
print(four_dividers(3))
