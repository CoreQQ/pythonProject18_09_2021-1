import math


def main():
    number = int(input('enter number'))

    fact = factorial(number)

    print('factorial is: ', fact)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
main()