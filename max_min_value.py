# Напишите программу, которая получает на вход три целых числа, по одному
# числу  в строке, и выводит на консоль в три строки сначала максимальное,
# потом  минимальное, после чего оставшееся число.
#
# На ввод могут подаваться и повторяющиеся числа.

a = int(input())
b = int(input())
c = int(input())
res = [a, b, c]
res_other = res.copy()
res_other.remove(max(res))
res_other.remove(min(res))

print(max(res))
print(min(res))
print(res_other[0])
