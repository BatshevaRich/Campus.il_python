import functools

def add(x, y):
    return x + y

def sum_of_digits(number):
    return functools.reduce(add, list(map(int, str(number))))

print(sum_of_digits(104))