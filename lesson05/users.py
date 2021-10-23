def get_cities_from_users(users):
    cities = []
    for user in users:
        cities.append(user[3])
    return tuple(cities)


def get_name_users_from_cities(users, city):
    names = []
    for user in users:
        if (user[3] == city):
            names.append(user[1])
    return tuple(names)



def get_ages_from_users(users):
    ages_list = []
    for user in users:
        ages_list.append(int(user[2]))
    ages = tuple(ages_list)
    return ages


def get_users_from_file(filename):
    users = []
    with open(filename, "r") as file_dig:
        for el in file_dig:
            elems = el.replace("\n", "").split(" ")
            users.append(tuple(elems))
    return users





def main():
    users = get_users_from_file("user1.txt")
    print(users)
    # users[2][3] = "Vasya"
    cities = get_cities_from_users(users)
    print(cities)
    cities_list = list(cities)
    print(cities_list)
    ages = get_ages_from_users(users)
    print(ages)
    # ages[1] = "Vasya"
    print(ages)
    print(max(ages))
    name_users = get_name_users_from_cities(users, "Poltava")
    print(name_users)
if __name__ == '__main__':
    users = [(1, "Name1", "Age1", "City1"),(2, "Name2", "Age2", "City2")]
    names = get_name_users_from_cities(users, "City1")
    print(names)