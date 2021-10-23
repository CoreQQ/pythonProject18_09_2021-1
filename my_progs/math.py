while True:
    print('**********MENU**********')
    print('   Choose your part!')
    print('1 - "+"')
    print('2 - "-"')
    print('3 - "*"')
    print('4 - "/"')
    chs = input('Choose: ')

    num1 = 1
    num2 = 2
    num3 = 3
    num4 = 4
    def rtrn():
        rtrn1 = input("do you want back to the menu? Enter 5")
        if rtrn1 == '5':
            return True


    if chs == "1":
        print('"+"')
        task01 = int(input("Enter first number"))
        task02 = int(input("Enter second number"))
        ans = task01 + task02
        print('Ansver: ', ans)
        print('________________________')
    elif chs == "2":
        print('"-"')
        task01 = int(input("Enter first number"))
        task02 = int(input("Enter second number"))
        ans = task01 - task02
        print('Ansver: ', ans)
        print('________________________')
    elif chs == "3":
        print('"*"')
        task01 = int(input("Enter first number"))
        task02 = int(input("Enter second number"))
        ans = task01 * task02
        print('Ansver: ', ans)
        print('________________________')
    elif chs == "4":
        print('"/"')
        task01 = int(input("Enter first number"))
        task02 = int(input("Enter second number"))
        ans = task01 / task02
        print('Ansver: ', ans)
        print('________________________')


