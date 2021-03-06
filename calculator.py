# Напишите простой калькулятор, который считывает с пользовательского ввода
# три  строки: первое число, второе число и операцию, после чего применяет
# операцию к введённым числам ("первое число" "операция" "второе число") и
# выводит результат на экран.
#
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
#
# Если выполняется деление и второе число равно 0, необходимо выводить строку
# "Деление на 0!".
#
# Обратите внимание, что на вход программе приходят вещественные числа.

print('Введите числа:')
a = float(input())
b = float(input())
print('''
Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.
Введите операцию:
''')
operation = input()

if (operation == '/' or operation == 'div' or operation == 'mod') and b == 0:
    print('Деление на 0!')
else:
    if operation == '/':
        print(a / b)
    elif operation == 'div':
        print(a // b)
    elif operation == 'mod':
        print(a % b)
    elif operation == '+':
        print(a + b)
    elif operation == '-':
        print(a - b)
    elif operation == '*':
        print(a * b)
    elif operation == 'pow':
        print(a ** b)

print('Введите числа:')
a = int(input())
b = int(input())
print('Поддерживаемые операции: +, -, /, *')
operation = input()

if operation == '+' or operation == '-' or operation == '*' or operation == '/':
    if operation == '/' and b == 0:
        print('На ноль делить нельзя!')
    elif operation == '+':
        print(a + b)
    elif operation == '-':
        print(a - b)
    elif operation == '*':
        print(a * b)
    else:
        print(a / b)
else:
    print('Неверная операция')