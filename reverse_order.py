num = int(input())
newnum = 0

while num != 0:
    last_digit = num % 10
    newnum = newnum * 10 + last_digit
    num = num // 10

print(newnum)
