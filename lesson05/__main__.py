from lesson05.users import *


def convert_list_to_str(elems, delimetr=" "):
    str_elems = ""
    for el in elems:
        str_elems+=str(el) + delimetr
    return str_elems


def convert_list_to_str_csv(elems):
    str_elems = ""
    for el in elems:
        str_elems+=str(el) + ";"
    return str_elems


def write_to_file_txt(filename):
    with open(filename, "w") as file_dig:
        for el in elems:
            file_dig.write(convert_list_to_str(el, delimetr=" "), + "\n")


def write_to_file_csv(filename):
    with open(filename, "w") as file_dig:
        for el in elems:
            file_dig.write(str(el) + "\n")


if __name__ == '__main__':
    # main()
    elems = [(1, "Name1", "Age1", "City1"), (2, "Name2", "Age2", "City2")]
    write_to_file_txt("user2.txt")
    write_to_file_csv("user2.csv")
    users_list = get_users_from_file("user2.csv", ";")
    print(users_list)