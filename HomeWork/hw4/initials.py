import def_main

def initials():
    first = input("Enter your name: ")
    middle = input("Enter your middle name: ")
    last = input("Enter your lastname: ")


    print("Your initials is: ")
    print(def_main.get_name_first_letters(first, middle, last))

initials()