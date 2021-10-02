from lesson02.tasklib import find_min_value, get_min_value


# Даны 4 числа типа int.

n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
n3 = int(input("Enter third number"))
n4 = int(input("Enter first number"))

#===math
min_value = min(n1, n2, n3, n4)
print("lib_min", min_value)
# Сравнить их и вывести наименьшее на консоль.
find_min_value(2,5,3,1)

min_num = get_min_value(n1, n2, n3, n4)
print("min_num=", min_num)

# 2. Вывести на консоль количество максимальных чисел среди этих четырех.

max_num = n1
if max_num < n2:
    max_num = n2
if max_num < n3:
    max_num = n3
if max_num < n4:
    max_num = n4

count_max = 0

if n1 == max_num:
    count_max+=1
if n2 == max_num:
    count_max+=1
if n3 == max_num:
    count_max+=1
if n4 == max_num:
    count_max+=1
print("count max=", count_max)
