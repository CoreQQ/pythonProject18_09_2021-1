import csv

if __name__ == '__main__':
    with open("sichen-zp-2019.csv", "r") as file_dig:
        second = []
        for row in file_dig:
            spl = float(row.split(',')[11]) #не могу найти проблему
            second.append(spl)
        print(second)

        lowest = min(second)
        print(lowest)
        highest = max(second)
        print(highest)