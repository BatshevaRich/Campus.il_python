shopping_list = input("Enter Shopping List ").split(',')

def illegal_choices(my_list):
    illegal = list()
    for element in my_list:
        if len(element) < 3 or not element.isalpha():
            illegal.append(element)
    return illegal

user = 1
while user:
    user_choice = input("enter your choice ")
    if user_choice == '1':
        print(shopping_list)
    elif user_choice == '2':
        print(len(shopping_list))
    elif user_choice == '3':
        if input("enter your search object ") in shopping_list:
            print(True)
    elif user_choice == '4':
        print(shopping_list.count(input("enter your search object ")))
    elif user_choice == '5':
        shopping_list.remove(input("enter object to remove "))
    elif user_choice == '6':
        shopping_list.append(input("enter object to add "))
    elif user_choice == '7':
        print(illegal_choices(shopping_list))
    elif user_choice == '8':
        shopping_list = list(set(shopping_list))
    elif user_choice == '9':
        user = 0


