n = int(input())
for i in range(1):
    for k in range(1, (n + 1) // 2 + 1):
        print('*' * k)
for i in range(1):
    for k in range((n + 1) // 2 - 1, 0, -1):
        print('*' * k)
