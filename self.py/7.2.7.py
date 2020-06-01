def arrow(my_char, max_length):
    shape = ''
    holder = 1
    while holder <= max_length:
        shape += my_char * holder + '\n'
        holder += 1
    holder = max_length - 1
    while holder > 0:
        shape += my_char * holder + '\n'
        holder -= 1
    return shape

def arrow2(my_char, max_length):
    shape = ''
    holder = 1
    while holder <= max_length * 2 - 1:
        if holder <= max_length: 
            print(my_char * holder)
        else:
            print(my_char * int(holder  / 2 + 1))
        holder += 1
    return shape

print(arrow('*', 5))
arrow2("*", 5)