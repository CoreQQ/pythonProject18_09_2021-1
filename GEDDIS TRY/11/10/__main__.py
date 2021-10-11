def main():
    count = 0
    my_string = input("Введите предложение: ")
    for ch in my_string:
        if ch == 'Т' or ch == "т":
            count += 1
    print("Word T takes: ", count, "parts")

main()

