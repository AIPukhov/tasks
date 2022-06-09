x = int(input())

if 1 <= x <= 10:
    if x % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= x <= 18:
    if x % 2 == 0:
        print('красный')
    else:
        print('черный')
elif 19 <= x <= 28:
    if x % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 29 <= x <= 36:
    if x % 2 == 0:
        print('красный')
    else:
        print('черный')
elif x == 0:
    print('зеленый')
else:
    print('ошибка ввода')