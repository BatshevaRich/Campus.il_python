user_temp = input("Insert the temperature you would like to convert: ")

temp_type = user_temp[-1].lower()
user_temp =float(user_temp[:-1])

if temp_type == 'f':
    print('{} C'.format((5 * user_temp - 160) / 9))
else:
    print('{} F'.format((9 * user_temp + (32 * 5)) / 5))