def stars(num):
    star = '*'
    space = ' '

    for i in range(num):
        space_len = num - (i + 1)

        print(space * space_len, end = '')
        print(star * (i + 1), end = '')
        print(star * i)


number = int(input())
stars(number)