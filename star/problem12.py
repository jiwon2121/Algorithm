def stars(num):
    count = 1
    interval = 1

    while count > 0:
        line = ' ' * (num - count) + '*' * count
        print(line)

        if count == num:
            interval = -1

        count += interval


number = int(input())
stars(number)