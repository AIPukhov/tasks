a = int(input())
b = int(input())
for i in range(a, b + 1):
    count = 0
    for k in range(1, b + 1):
        if i % k == 0:
            count += 1
        if count > 2:
            break
    if count == 2:
        print(i)
