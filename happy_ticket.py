# Паша очень любит кататься на общественном транспорте, а получая билет, сразу
# проверяет, счастливый ли ему попался. Билет считается счастливым, если сумма
# первых трех цифр совпадает с суммой последних трех цифр номера билета.
#
# Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
# которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают,
# и "Обычный", если суммы различны.
#
# На вход программе подаётся строка из шести цифр.
#
# Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.


ticket = list(map(int, input()))

sum_1 = ticket[0] + ticket[1] + ticket[2]
sum_2 = ticket[3] + ticket[4] + ticket[5]

if sum_1 == sum_2:
    print('Счастливый')
else:
    print('Обычный')
