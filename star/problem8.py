def stars(num):
    star = '*'
    blank = ' '
    count = 1
    interval = 1

    while count != 0:
        line = (star * count) + (blank * (num-count) * 2) + (star * count)
        print(line)

        if count == num:
            interval = -1

        count += interval


number = int(input())
stars(number)