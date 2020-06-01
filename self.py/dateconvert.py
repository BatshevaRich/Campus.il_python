import calendar

user_input = input("Enter a date: ")
# 01/01/2000
year = int(user_input[-4:])

month = int(user_input[3:5])

day = int(user_input[:2])

print(calendar.day_name[calendar.weekday(year, month, day)])