if __name__ == '__main__':
    n = 20
    m = 20
    for i in range (0,n, 1):
        for j in range(0,m, 1):
            if i == (n)/2 or j ==n/2+i or j ==n/2-i:
                print("*",end="")
            else:
                print(" ",end="")

        print()

