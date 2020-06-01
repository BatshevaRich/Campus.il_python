def seven_boom(end_number):
    boom = list()
    for number in range(end_number):
        if number % 7 == 0 or '7' in set(str(number)):
            boom.append('BOOM')          
        else:
            boom.append(number)
    return boom
print(seven_boom(18))