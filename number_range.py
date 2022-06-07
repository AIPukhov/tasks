# Программа, принимающая на вход целое число, которая выводит True,
# если переданное значение попадает в заданный интервал и False в противном
# случае.

integer = int(input())

if -15 < integer <= 12 or 14 < integer < 17 or 19 <= integer < float('inf'):
    print(True)
else:
    print(False)
