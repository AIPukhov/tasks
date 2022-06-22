import math
x = input()
sum_x = sum(list(map(int, x)))  # сумму его цифр
len_x = len(list(x))  # количество цифр в нем
prod_x = math.prod(list(map(int, x)))  # произведение его цифр
average_x = sum(list(map(int, x))) / len(list(x))  # среднее арифметическое его цифр
first_x = x[0]  # его первую цифру
sum_first_end = int(x[0]) + int(x[-1])  # сумму его первой и последней цифры
print(sum_x)
print(len_x)
print(prod_x)
print(average_x)
print(first_x)
print(sum_first_end)