def numbers_letters_count(my_str):
    total = list([0, 0])
    for element in my_str:
        if element.isdigit():
            total[0] = total[0] +1
        else:
            total[1] = total[1] + 1
    return total

print(numbers_letters_count("Python 3.6.3"))