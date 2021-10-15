def main():
    num1 = int(input("Enter full number"))
    num2 = int(input("enter second full number"))

    print("gcd is: ")
    print("these two numbers", gcd(num1, num2))

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)
main()