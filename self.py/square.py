def squared_numbers(start, stop):
    squared = list()
    while start <= stop:
        squared.append(start **2)
        start += 1
    return squared

print(squared_numbers(4, 8))
print(squared_numbers(-3, 3))
        