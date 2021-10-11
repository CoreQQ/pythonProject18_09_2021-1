import login

def main():
    first = input("Введите свое имя")
    last = input("Введите свою фамилию")
    idnumber = input("введите свой номер студента")

    print('Ваше имя для входа в систему')
    print(login.get_login_name(first, last, idnumber))

main()