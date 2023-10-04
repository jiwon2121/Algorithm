def stars(num):
    star = '*'
    blank = ' '
    count = num
    interval = -1

    while count <= num:
        blank_len = num - count
        star_len = count * 2 - 1 

        line = (blank * blank_len) + (star * star_len)
        print(line)

        if count == 1:
            interval = 1

        count += interval


number = int(input())
stars(number)