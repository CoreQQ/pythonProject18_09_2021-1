# 1. Прочитать из файла info.json данные в dict
# 2. Отобразить количество хобби сотрудника и вывести их на екран
# 3. Сколько детей у сотрудника
# 4. Вывести имя старшего ребенка
# 5. Добавить в dict сотрудника ключ "email": jane@company.com , "phone": 123456
# и сохранить в новый файл info2.json
import json


def det_dict_from_file(filename):
    with open(filename, "r") as file_users:
        users_json = json.load(file_users)
        return users_json


def get_max_age_child(children_list):
    global max_age_child
    max_age_child = children_list[0]
    for child in children_list:
        if (max_age_child['age'] < child['age']):
            max_age_child = child
    return max_age_child

if __name__ == '__main__':
    users_dict = det_dict_from_file("info.json")
    print(users_dict)

    hobby_list = users_dict["hobbies"]
    print(hobby_list)
    print(len(hobby_list))

    children_list = users_dict['children']
    print(len(children_list))

    print(get_max_age_child(children_list))


