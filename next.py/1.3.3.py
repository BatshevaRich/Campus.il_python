def is_funny(string):
    return all(c in ('a', 'h') for c in string)
    # return [char for char in string if char != 'h' if char != 'a']

print(is_funny("hahahahahaha"))
print(is_funny("hahav"))
