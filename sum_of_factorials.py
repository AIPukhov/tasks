n = int(input())
total = 0
while n:
    p = 1
    i = 1
    n2 = n
    while i <= n2:
        p *= i
        i += 1
    total += p
    n -= 1
print(total)
