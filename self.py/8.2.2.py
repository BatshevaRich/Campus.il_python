def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, reverse=True, key= lambda p: p[1])

products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))