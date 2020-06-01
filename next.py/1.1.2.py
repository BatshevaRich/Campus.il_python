def multiply_letters(a):
    return a * 2
def double_letter(my_str):
    return ''.join(map(multiply_letters, my_str))

print(double_letter("python"))
print(double_letter("we are the champions!"))