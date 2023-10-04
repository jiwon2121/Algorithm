def stars(num):
    star = '*'
    blank = ' '
    count = 1
    interval = 1

    while count != 0:
        line = blank * (num - count) + star * (count * 2 - 1)
        print(line)

        if count == num:
            interval = -1

        count += interval


number = int(input())
stars(number)