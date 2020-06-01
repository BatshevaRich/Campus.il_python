
def combine_coins(symbol, numbers):
    return ', '.join([symbol + str(i) for i in numbers])
# return ', '.join(map(lambda s, n: s + str(n), [coin for i in numbers], numbers))


print(combine_coins('$', range(5)))