def last_early(my_str):
    if my_str[-1].lower() in my_str[:-1].lower():
        return True
    return False

print(last_early("happy birthday"))
print(last_early("best of luck"))
print(last_early("Wow"))
print(last_early("X"))
