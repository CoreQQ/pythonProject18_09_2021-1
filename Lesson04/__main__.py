if __name__ == '__main__':
    arr = [1,2,43,2,3,2,4,2,332,4,23,4,234,3]
    count = 0
    for j in range (len(arr)-1):
        for i in range(len(arr)-1-j):
            count = 1
            if arr[i]> arr[i+1]:
                temp = arr[1]
                arr[i] = arr[i+1]
                arr[i+1] = temp

print(arr)
