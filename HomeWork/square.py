def main():
    side1 = int(input("Напишите число первой стороны первой фигуры"))
    side1_1 = int(input("Напишите число второй стороны первой фигуры"))
    square1 = side1 * side1_1
    side2 = int(input("Напишите число первой стороны второй фигуры"))
    side2_1 = int(input("Напишите число второй стороны второй фигуры"))
    square2 = side2 * side2_1

    if square1 > square2:
        print("Первая фигура больше!")
    elif square1 < square2:
        print("вторая фигура больше!")
    elif square1 == square2:
        print("Фигуры одинаковые!")
main()
